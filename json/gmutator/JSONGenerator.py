# Generated by Grammarinator 19.3.post165+gf23ccaf

import itertools

from math import inf
from grammarinator.runtime import *

class JSONGenerator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def json(self, parent=None):
        with RuleContext(self, UnparserRule(name='json', parent=parent)) as current:
            self.value(parent=current)
            self.EOF(parent=current)
            return current
    json.min_depth = 1

    def obj(self, parent=None):
        with RuleContext(self, UnparserRule(name='obj', parent=parent)) as current:
            with AlternationContext(self, [2, 0, 2], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='{', parent=current)
                    self.pair(parent=current)
                    if self._max_depth >= 2:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            UnlexerRule(src=',', parent=current)
                            self.pair(parent=current)
                    UnlexerRule(src='}', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='{', parent=current)
                    UnlexerRule(src='}', parent=current)
                elif choice0 == 2:
                    UnlexerRule(src='{', parent=current)
                    self.pair(parent=current)
                    if self._max_depth >= 2:
                        for _ in self._model.quantify(current, 1, min=0, max=inf):
                            UnlexerRule(src=',', parent=current)
                            self.pair(parent=current)
                    UnlexerRule(src='}', parent=current)
                    UnlexerRule(src='{', parent=current)
                    self.pair(parent=current)
                    if self._max_depth >= 2:
                        for _ in self._model.quantify(current, 2, min=0, max=inf):
                            UnlexerRule(src=',', parent=current)
                            self.pair(parent=current)
                    UnlexerRule(src='}', parent=current)
            return current
    obj.min_depth = 0

    def pair(self, parent=None):
        with RuleContext(self, UnparserRule(name='pair', parent=parent)) as current:
            self.STRING(parent=current)
            UnlexerRule(src=':', parent=current)
            self.value(parent=current)
            return current
    pair.min_depth = 1

    def arr(self, parent=None):
        with RuleContext(self, UnparserRule(name='arr', parent=parent)) as current:
            with AlternationContext(self, [1, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='[', parent=current)
                    self.value(parent=current)
                    if self._max_depth >= 1:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            UnlexerRule(src=',', parent=current)
                            self.value(parent=current)
                    UnlexerRule(src=']', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='[', parent=current)
                    UnlexerRule(src=']', parent=current)
            return current
    arr.min_depth = 0

    def value(self, parent=None):
        with RuleContext(self, UnparserRule(name='value', parent=parent)) as current:
            with AlternationContext(self, [1, 2, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                src = [None, None, None, None, 'true', 'false', 'null'][choice0]
                rule = [self.STRING, self.NUMBER, self.obj, self.arr, None, None, None][choice0]
                if src is not None:
                    UnlexerRule(src=src, parent=current)
                else:
                    rule(parent=current)
            return current
    value.min_depth = 0

    def STRING(self, parent=None):
        with RuleContext(self, UnlexerRule(name='STRING', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['"', 'u'][choice0], parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    with AlternationContext(self, [1, 0], [1, 1]) as weights1:
                        choice1 = self._model.choice(current, 1, weights1)
                        if choice1 == 0:
                            self.ESC(parent=current)
                        elif choice1 == 1:
                            if self._max_depth >= 1:
                                for _ in self._model.quantify(current, 1, min=0, max=inf):
                                    self.SAFECODEPOINT(parent=current)
            UnlexerRule(src='"', parent=current)
            return current
    STRING.min_depth = 0

    def ESC(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ESC', parent=parent)) as current:
            UnlexerRule(src='\\', parent=current)
            with AlternationContext(self, [0, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
                elif choice0 == 1:
                    self.UNICODE(parent=current)
            return current
    ESC.min_depth = 0

    def UNICODE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='UNICODE', parent=parent)) as current:
            UnlexerRule(src='u', parent=current)
            self.HEX(parent=current)
            self.HEX(parent=current)
            self.HEX(parent=current)
            self.HEX(parent=current)
            return current
    UNICODE.min_depth = 1

    def HEX(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEX', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[2]), parent=current)
            return current
    HEX.min_depth = 0

    def SAFECODEPOINT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SAFECODEPOINT', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[3]), parent=current)
            return current
    SAFECODEPOINT.min_depth = 0

    def NUMBER(self, parent=None):
        with RuleContext(self, UnlexerRule(name='NUMBER', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    UnlexerRule(src='-', parent=current)
            self.INT(parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    UnlexerRule(src='.', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 2, min=1, max=inf):
                            UnlexerRule(src=self._model.charset(current, 0, self._charsets[4]), parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 3, min=0, max=1):
                    self.EXP(parent=current)
            return current
    NUMBER.min_depth = 1

    def INT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='INT', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='0', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[5]), parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            UnlexerRule(src=self._model.charset(current, 1, self._charsets[6]), parent=current)
            return current
    INT.min_depth = 0

    def EXP(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EXP', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[7]), parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[8]), parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 2, self._charsets[9]), parent=current)
            return current
    EXP.min_depth = 0

    def WS(self, parent=None):
        with RuleContext(self, UnlexerRule(name='WS', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[10]), parent=current)
            return current
    WS.min_depth = 0

    _default_rule = json

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(34, 35), range(47, 48), range(92, 93), range(98, 99), range(102, 103), range(110, 111), range(114, 115), range(116, 117)])),
        2: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        3: list(itertools.chain.from_iterable([range(32, 34), range(35, 92), range(93, 127)])),
        4: list(itertools.chain.from_iterable([range(48, 58)])),
        5: list(itertools.chain.from_iterable([range(49, 58)])),
        6: list(itertools.chain.from_iterable([range(48, 58)])),
        7: list(itertools.chain.from_iterable([range(69, 70), range(101, 102)])),
        8: list(itertools.chain.from_iterable([range(43, 44), range(45, 46)])),
        9: list(itertools.chain.from_iterable([range(48, 58)])),
        10: list(itertools.chain.from_iterable([range(9, 10), range(10, 11), range(13, 14), range(32, 33)])),
    }
