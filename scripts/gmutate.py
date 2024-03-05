import sys
import re
import random
import os
from functools import cached_property

def decision(probability):
    return random.random() < probability

class Grammar:

  def __init__(self, filename):
    self.filename = filename
    if 'Parser' in filename:
      self.gtype = 'Parser'
      self.borrowed_tokens = []
    elif 'Lexer' in filename:
      self.gtype = 'Lexer'
    else:
      self.gtype = 'Mix'
    with open(filename,'r') as f:
      self.strg = GrammarMutator.intro.sub('\\1', f.read())
      self.strg = GrammarMutator.linecomment.sub('\n', self.strg)
    
  @cached_property
  def tokens(self):
    words = re.findall(r'(fragment |\n)([A-Z]+)\n', self.strg)
    literals = re.findall(r"([ (]['][^'\\]+(?:\\.[^'\\]*)*['])", self.strg)
    res = []
    for sub in words:
      res.append(sub[1])
    for l in literals:
      res.append(l[1:])
    return res

  @cached_property
  def non_terminals(self):
    words = re.findall(r'\n[a-z]+\n', self.strg)
    res = []
    for sub in words:
      res.append(sub.replace("\n", ""))
    return res

  def reset(self):
    self._rules = self.strg.split(' :')

  @property
  def rules(self):
    return(self._rules)

  @cached_property
  def n_rules(self):
    return(len(self.rules))
    
  @cached_property
  def weights(self):
    mutable_rules = self.rules[1:]
    weights = [len(rule) for rule in mutable_rules]
    return(weights)

class GrammarMutator(Grammar):

  mutation = 0
  
  def __init__(self, filename):
    super().__init__(filename) 
    self.forbiden = [' open_tag', ' deepcopy']  
    self.reset() 

  @property
  def string(self):
    return ' :'.join(self.rules)
  
  def change(self, i, value):
    self._rules[i] = value

  def mutate(self, n=3):
    mutated_rules = set()
    self.m = 0

    while(self.m<n):
      #i = random.randrange(1, self.n_rules)
      
      i_list = [i for i in range(1, self.n_rules)]
      
      i = random.choices(i_list, weights=self.weights, k=1)[0]

      merge = decision(0.2)
      
      if merge:
        t = self.merge_word(self.rules, i)

      else:
        lst = [self.rep_literal_func, self.replace_operator_func, self.exclude_func, self.alt_func, self.rep_sr_func, self.rep_word_func]

        func = random.choice(lst)
        t = func(self.rules[i])

      if t[1] > 0: # If one or more locations were edited
        self.m += t[1]
        mutated_rules.add(i)
        self.change(i, t[0]) # Update the rules array with the new mutation
        
  linecomment = re.compile('\n//[^\n]+\n')
  intro = re.compile('(?s).*((\ngrammar|parser grammar|lexer grammar) [A-z]+;){1}')

  # Regexes and their replacements: (name, regex, replacement)
  # These patterns are for changing repetition orparators or replcaing single characters
  replace_operator = ('replace_operator', re.compile('([^<}])[\+\?]'), '\\1*')
  exclude = ('exclude', re.compile('[~][ ]*[\[(].*?[\])]'), r'[\\u0000-\\uFFFE]')
  anychar = ('anychar', re.compile("([^'~])\[.+?\]"), '\\1.')
  rep_sr = ('rep_sr', re.compile('[\)]([ \n])'), ')*\\1')
  rep_word = ('rep_word', re.compile('(?<!mode)(?<!->)(?<!pushMode)([ (](?!self)(?!version)[a-zA-Z][A-z0-9]+)'), '\\1*')
  rep_literal = ('rep_literal', re.compile(r"([ (]['][^'\\]+(\\.[^'\\]*)*['])[\+\?]?"), '\\1*')

  # These patterns are for cleaning douple rep op
  single_rep_op = ('single_rep_op', re.compile('[\*][\+\?\*]'), '*')
  
  # These patterns are for replacing a token/non-terminal with a random token/non-terminal
  replace_word = ('replace_word', re.compile("(?<!mode)(?<!->)(?<!pushMode)(?<!channel)(?<!more,)([ (])([a-zA-Z][A-z0-9]+|['].*?['])"), '\\1XXX') #       ([ (](?!skip))[A-z][A-z]+
  
  def rep_literal_func(self, rule):
    # Find literals enclosed in single quotes. 
    # Escaped characters are allowed. But the closing quote cannot be escaped.
    words = re.findall(r"([ (]['][^'\\]+(?:\\.[^'\\]*)*['])[\+\?]?", rule)
    # Adding a non-capturing group (?:...) to prevent split() from returning delimiters
    elements = re.split(r"(?:[ (]['][^'\\]+(?:\\.[^'\\]*)*['])[\+\?]?", rule)
    t = self.pick_mutate(rule, self.rep_literal, words, elements)
    return t
  
  # Replace symbol '?' or '+' with '*'
  def replace_operator_func(self, rule):
    words = re.findall('[^<}][\+\?]', rule)
    elements = re.split('[^<}][\+\?]', rule)
    t = self.pick_mutate(rule, self.replace_operator, words, elements)
    return t
   
  def exclude_func(self, rule):
    words = re.findall('[~][ ]*[\[(].*?[\])]', rule)
    elements = re.split('[~][ ]*[\[(].*?[\])]', rule)
    t = self.pick_mutate(rule, self.exclude, words, elements)
    return t
    
  def alt_func(self, rule):
    # First check if there are inline alts
    # Warning: Nested brackets won't work, since regex is looking for first ')'
    words = re.findall('[(].*?[|].*?[)](?![\'])', rule) # [(](.*?[|].*?){1}[^\'][)]
    elements = re.split('[(].*?[|].*?[)](?![\'])', rule)
    if len(elements) > 1: # In case there is inline alts, remove outer brackets and apply function again.
      rule_a = words[0][1:-1]
      mword = self.alt_func(rule_a)
      words[0] = '(' + mword[0] + ')'
      
      i = 0
      string = ''
      while i < len(words): # Join the string bits back together
        string = string + elements[i] + words[i]
        i += 1
      string = string + elements[i]
      t = (string, mword[1])
      return t

    # In case no inline alts, proceed with mutation
    elements = re.split(';\n', rule)
    alts = re.split('[|]', elements[0])
    
    if len(alts) == 1:
      # Only 1 alt, so no mutation
      return (rule, 0)
    
    alt_a = random.choice(alts)
    alt_b = random.choice(alts)
    if alts[-1][-1] != ' ': alts[-1] += ' '
    alts.append(' ' + alt_a.strip() + ' ' + alt_b.strip())
    elements[0] = '|'.join(alts)
    newrule = ';\n'.join(elements)
    t = (newrule, 1)
    return t
    
  def anychar_func(self, rule):
    words = re.findall("[^']\[.+?\]", rule)
    elements = re.split("[^']\[.+?\]", rule)
    t = self.pick_mutate(rule, self.anychar, words, elements)
    return t
  
  
  def rep_sr_func(self, rule):
    words = re.findall('[\)][ \n]', rule)
    elements = re.split('[\)][ \n]', rule)
    t = self.pick_mutate(rule, self.rep_sr, words, elements)
    return t
    
  # The core mutate function
  def pick_mutate(self, rule, p, words, elements, sub=''):
    n = len(words)
    if n == 0:
      t =  (rule, 0)
    elif n == 1:
      t = p[1].subn(p[2], rule, 1)
      return t
    else:
      while True:
        pos = random.randrange(n)
        if words[pos] not in self.forbiden:
          break
      # Mutate substing words[pos], then update the list, then concatenate the list.
      mword = p[1].subn(p[2], words[pos], 1)
      words[pos] = mword[0]

      i = 0
      string = ''
      while i < len(words): # Join the string bits back together
        string = string + elements[i] + words[i]
        i += 1
      string = string + elements[i]
      t = (string, mword[1])
    return t
    

  def rep_word_func(self, rule):
    rule_frag = rule.split('fragment')
    words = re.findall('(?<!mode)(?<!->)(?<!pushMode)([ (](?!self)(?!version)[a-zA-Z][A-z0-9]+)', rule_frag[0])
    elements = re.split('(?<!mode)(?<!->)(?<!pushMode)(?:[ (](?!self)(?!version)[a-zA-Z][A-z0-9]+)', rule_frag[0])
    t = self.pick_mutate(rule_frag[0], self.rep_word, words, elements)
    tx = self.single_rep_op[1].subn(self.single_rep_op[2], t[0])
    rule_frag[0] = tx[0]
    newrule = 'fragment'.join(rule_frag)
    if tx[1] == 0: 
      t = (newrule, t[1])
    else: # 0 successful mutations because mutations are non valid, that is, it resulted in double rep ops
      t = (newrule, 0)
    return t
  
  
  def merge_word(self, rules, i):
    rule = rules[i]
    rule_frag = rule.split('fragment')
    # Find non-terminal, token or literal, and replace.
    tuples = re.findall(r"(?<!mode)(?<!->)(?<!pushMode)(?<!channel)(?<!more,)([ (])([a-zA-Z][A-z0-9]+|['].*?['])", rule_frag[0])
    elements = re.split(r"(?<!mode)(?<!->)(?<!pushMode)(?<!channel)(?<!more,)[ (](?:[a-zA-Z][A-z0-9]+|['].*?['])", rule_frag[0])
    
    # tuples has a list of tuples. We make it a flat list.
    words = []
    for word in tuples:
        words.append(word[0]+word[1])

    if self.gtype == 'Lexer':
      choices = self.tokens
    else:
      # We need to check if the rule name (parent) is a terminal or non-terminal. In order to avoid placing a non-terminal in the definition of a terminal. To comply with antlr syntax.
      words_last_rule = re.findall('[a-zA-Z]+', rules[i-1])
      rule_name = words_last_rule[-1]
      if rule_name[0].isupper(): # Parent is a terminal
        choices = self.tokens
      else:
        choices = self.tokens+self.non_terminals

    self.replace_word = (self.replace_word[0], self.replace_word[1], '\\1(\\2 | '+random.choice(choices)+')')
    x = self.pick_mutate(rule_frag[0], self.replace_word, words, elements)

    rule_frag[0] = x[0]
    newrule = 'fragment'.join(rule_frag)

    t = (newrule, x[1])
    return t 

  def choose(self):
    return random.choice(self.lst)
	

if __name__ == '__main__':
    subjectpath = sys.argv[1]
    subject = subjectpath.split('/')[1]
    gfile = subjectpath.split('/')[2]
    parg = GrammarMutator(subjectpath)
    
    
    dest_folder = sys.argv[2]
    seed = int(sys.argv[3])
    random.seed(seed)

    mutation_n = 3 #random.randrange(3, 23)
      
    no_lexer_grammar = True
    
    if len(sys.argv) == 5:
      no_lexer_grammar = False
      lexerpath = sys.argv[4]
      subject = lexerpath.split('/')[1]
      lgfile = lexerpath.split('/')[2]
      larg = GrammarMutator(lexerpath)
           
    if no_lexer_grammar:
      parg.mutate(mutation_n)
    else:
      die = random.choice([0, 1])
      if die == 0:
        parg.mutate(mutation_n)
      else:
        larg.mutate(mutation_n)
        

    
    nfile1 = '../' + subject + '/gmutator/' + dest_folder + '/' + gfile
    fout = open(nfile1, "wt")
    fout.write(parg.string)
    fout.close()
    parg.reset()
    
    if not no_lexer_grammar:
      nfile1 = '../' + subject + '/gmutator/' + dest_folder + '/' + lgfile
      fout = open(nfile1, "wt")
      fout.write(larg.string)
      fout.close()
      larg.reset()

