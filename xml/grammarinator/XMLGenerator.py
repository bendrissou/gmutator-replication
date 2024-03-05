# Generated by Grammarinator 19.3.post165+gf23ccaf

import itertools

from math import inf
from grammarinator.runtime import *


from copy import deepcopy

class XMLGenerator(Generator):

    def _endOfXmlElement(self):
        pass

    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def COMMENT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='COMMENT', parent=parent)) as current:
            UnlexerRule(src='<!--', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[0]), parent=current)
            UnlexerRule(src='-->', parent=current)
            return current
    COMMENT.min_depth = 0

    def CDATA(self, parent=None):
        with RuleContext(self, UnlexerRule(name='CDATA', parent=parent)) as current:
            UnlexerRule(src='<![CDATA[', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[0]), parent=current)
            UnlexerRule(src=']]>', parent=current)
            return current
    CDATA.min_depth = 0

    def DTD(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DTD', parent=parent)) as current:
            UnlexerRule(src='<!', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[0]), parent=current)
            UnlexerRule(src='>', parent=current)
            return current
    DTD.min_depth = 0

    def EntityRef(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EntityRef', parent=parent)) as current:
            UnlexerRule(src='&', parent=current)
            self.Name(parent=current)
            UnlexerRule(src=';', parent=current)
            return current
    EntityRef.min_depth = 2

    def CharRef(self, parent=None):
        with RuleContext(self, UnlexerRule(name='CharRef', parent=parent)) as current:
            with AlternationContext(self, [1, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='&#', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 0, min=1, max=inf):
                            self.DIGIT(parent=current)
                    UnlexerRule(src=';', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='&#x', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 1, min=1, max=inf):
                            self.HEXDIGIT(parent=current)
                    UnlexerRule(src=';', parent=current)
            return current
    CharRef.min_depth = 1

    def SEA_WS(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SEA_WS', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    with AlternationContext(self, [0, 0, 0], [1, 1, 1]) as weights0:
                        choice0 = self._model.choice(current, 0, weights0)
                        if choice0 == 0:
                            UnlexerRule(src=' ', parent=current)
                        elif choice0 == 1:
                            UnlexerRule(src='\t', parent=current)
                        elif choice0 == 2:
                            if self._max_depth >= 0:
                                for _ in self._model.quantify(current, 1, min=0, max=1):
                                    UnlexerRule(src='\r', parent=current)
                            UnlexerRule(src='\n', parent=current)
            return current
    SEA_WS.min_depth = 0

    def OPEN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='OPEN', parent=parent)) as current:
            UnlexerRule(src='<', parent=current)
            return current
    OPEN.min_depth = 0

    def XMLDeclOpen(self, parent=None):
        with RuleContext(self, UnlexerRule(name='XMLDeclOpen', parent=parent)) as current:
            UnlexerRule(src='<?xml', parent=current)
            self.S(parent=current)
            return current
    XMLDeclOpen.min_depth = 1

    def SPECIAL_OPEN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SPECIAL_OPEN', parent=parent)) as current:
            UnlexerRule(src='<?', parent=current)
            self.Name(parent=current)
            return current
    SPECIAL_OPEN.min_depth = 2

    def TEXT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='TEXT', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            return current
    TEXT.min_depth = 0

    def CLOSE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='CLOSE', parent=parent)) as current:
            UnlexerRule(src='>', parent=current)
            return current
    CLOSE.min_depth = 0

    def SPECIAL_CLOSE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SPECIAL_CLOSE', parent=parent)) as current:
            UnlexerRule(src='?>', parent=current)
            return current
    SPECIAL_CLOSE.min_depth = 0

    def SLASH_CLOSE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SLASH_CLOSE', parent=parent)) as current:
            UnlexerRule(src='/>', parent=current)
            return current
    SLASH_CLOSE.min_depth = 0

    def SLASH(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SLASH', parent=parent)) as current:
            UnlexerRule(src='/', parent=current)
            return current
    SLASH.min_depth = 0

    def EQUALS(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EQUALS', parent=parent)) as current:
            UnlexerRule(src='=', parent=current)
            return current
    EQUALS.min_depth = 0

    def STRING(self, parent=None):
        with RuleContext(self, UnlexerRule(name='STRING', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='"', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            UnlexerRule(src=self._model.charset(current, 0, self._charsets[2]), parent=current)
                    UnlexerRule(src='"', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='\'', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 1, min=0, max=inf):
                            UnlexerRule(src=self._model.charset(current, 1, self._charsets[3]), parent=current)
                    UnlexerRule(src='\'', parent=current)
            return current
    STRING.min_depth = 0

    def Name(self, parent=None):
        with RuleContext(self, UnlexerRule(name='Name', parent=parent)) as current:
            self.NameStartChar(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.NameChar(parent=current)
            return current
    Name.min_depth = 1

    def S(self, parent=None):
        with RuleContext(self, UnlexerRule(name='S', parent=parent)) as current:
            UnlexerRule(src=' version="1.0"', parent=current)
            return current
    S.min_depth = 0

    def HEXDIGIT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEXDIGIT', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[4]), parent=current)
            return current
    HEXDIGIT.min_depth = 0

    def DIGIT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DIGIT', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[5]), parent=current)
            return current
    DIGIT.min_depth = 0

    def NameChar(self, parent=None):
        with RuleContext(self, UnlexerRule(name='NameChar', parent=parent)) as current:
            with AlternationContext(self, [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                src = [None, '-', '_', '.', None][choice0]
                rule = [self.NameStartChar, None, None, None, self.DIGIT][choice0]
                if src is not None:
                    UnlexerRule(src=src, parent=current)
                else:
                    rule(parent=current)
            return current
    NameChar.min_depth = 0

    def NameStartChar(self, parent=None):
        with RuleContext(self, UnlexerRule(name='NameStartChar', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[6]), parent=current)
            return current
    NameStartChar.min_depth = 0

    def PI(self, parent=None):
        with RuleContext(self, UnlexerRule(name='PI', parent=parent)) as current:
            UnlexerRule(src='?>', parent=current)
            return current
    PI.min_depth = 0

    def IGNORE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='IGNORE', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[0]), parent=current)
            return current
    IGNORE.min_depth = 0

    def document(self, parent=None):
        with RuleContext(self, UnparserRule(name='document', parent=parent)) as current:
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.prolog(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 1, min=0, max=inf):
                    self.misc(parent=current)
            self.element(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 2, min=0, max=inf):
                    self.misc(parent=current)
            self.EOF(parent=current)
            return current
    document.min_depth = 3

    def prolog(self, parent=None):
        with RuleContext(self, UnparserRule(name='prolog', parent=parent)) as current:
            self.XMLDeclOpen(parent=current)
            self.SPECIAL_CLOSE(parent=current)
            return current
    prolog.min_depth = 2

    def content(self, parent=None):
        with RuleContext(self, UnparserRule(name='content', parent=parent)) as current:
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.chardata(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 1, min=0, max=inf):
                    with AlternationContext(self, [3, 3, 1, 1], [1, 1, 1, 1]) as weights0:
                        choice0 = self._model.choice(current, 0, weights0)
                        [self.element, self.reference, self.CDATA, self.COMMENT][choice0](parent=current)
                    if self._max_depth >= 2:
                        for _ in self._model.quantify(current, 2, min=0, max=1):
                            self.chardata(parent=current)
            return current
    content.min_depth = 0

    def element(self, parent=None):
        local_ctx = dict(open_tag=None)
        with RuleContext(self, UnparserRule(name='element', parent=parent)) as current:
            with AlternationContext(self, [2, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='<', parent=current)
                    self.Name(parent=current)
                    local_ctx['open_tag'] = current.last_child
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            self.attribute(parent=current)
                    UnlexerRule(src='>', parent=current)
                    self.content(parent=current)
                    UnlexerRule(src='<', parent=current)
                    UnlexerRule(src='/', parent=current)
                    self.Name(parent=current)
                    current.last_child = deepcopy(local_ctx['open_tag'])
                    UnlexerRule(src='>', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='<', parent=current)
                    self.Name(parent=current)
                    local_ctx['open_tag'] = current.last_child
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 1, min=0, max=inf):
                            self.attribute(parent=current)
                    UnlexerRule(src='/>', parent=current)
            return current
    element.min_depth = 2

    def reference(self, parent=None):
        with RuleContext(self, UnparserRule(name='reference', parent=parent)) as current:
            with AlternationContext(self, [3, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.EntityRef, self.CharRef][choice0](parent=current)
            return current
    reference.min_depth = 2

    def attribute(self, parent=None):
        with RuleContext(self, UnparserRule(name='attribute', parent=parent)) as current:
            self.Name(parent=current)
            UnlexerRule(src='=', parent=current)
            self.STRING(parent=current)
            return current
    attribute.min_depth = 2

    def chardata(self, parent=None):
        with RuleContext(self, UnparserRule(name='chardata', parent=parent)) as current:
            with AlternationContext(self, [1, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.TEXT, self.SEA_WS][choice0](parent=current)
            return current
    chardata.min_depth = 1

    def misc(self, parent=None):
        with RuleContext(self, UnparserRule(name='misc', parent=parent)) as current:
            with AlternationContext(self, [1, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.COMMENT, self.SEA_WS][choice0](parent=current)
            return current
    misc.min_depth = 1

    _default_rule = document

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(32, 38), range(39, 60), range(61, 127)])),
        2: list(itertools.chain.from_iterable([range(32, 34), range(35, 60), range(61, 127)])),
        3: list(itertools.chain.from_iterable([range(32, 39), range(40, 60), range(61, 127)])),
        4: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        5: list(itertools.chain.from_iterable([range(48, 58)])),
        6: list(itertools.chain.from_iterable([range(58, 59), range(65, 91), range(97, 123)])),
    }
