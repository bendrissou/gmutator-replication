# Generated by Grammarinator 19.3.post165+gf23ccaf

import itertools

from math import inf
from grammarinator.runtime import *


import random

class urlGenerator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def url(self, parent=None):
        with RuleContext(self, UnparserRule(name='url', parent=parent)) as current:
            self.uri(parent=current)
            self.EOF(parent=current)
            return current
    url.min_depth = 5

    def uri(self, parent=None):
        with RuleContext(self, UnparserRule(name='uri', parent=parent)) as current:
            self.scheme(parent=current)
            UnlexerRule(src='://', parent=current)
            if self._max_depth >= 4:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.login(parent=current)
            self.host(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    UnlexerRule(src=':', parent=current)
                    self.port(parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 2, min=0, max=1):
                    UnlexerRule(src='/', parent=current)
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 3, min=0, max=1):
                            self.path(parent=current)
            if self._max_depth >= 5:
                for _ in self._model.quantify(current, 4, min=0, max=1):
                    self.query(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 5, min=0, max=1):
                    self.frag(parent=current)
            return current
    uri.min_depth = 4

    def scheme(self, parent=None):
        with RuleContext(self, UnparserRule(name='scheme', parent=parent)) as current:
            with AlternationContext(self, [0, 0, 0], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['ftp', 'http', 'https'][choice0], parent=current)
            return current
    scheme.min_depth = 0

    def host(self, parent=None):
        with RuleContext(self, UnparserRule(name='host', parent=parent)) as current:
            self.hostname(parent=current)
            return current
    host.min_depth = 3

    def hostname(self, parent=None):
        with RuleContext(self, UnparserRule(name='hostname', parent=parent)) as current:
            with AlternationContext(self, [3, 3, 2], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.hostname_DomainNameOrIPv4Host, self.hostname_IPv4Host, self.hostname_IPv6Host][choice0](parent=current)
            return current
    hostname.min_depth = 2

    def v4host(self, parent=None):
        with RuleContext(self, UnparserRule(name='v4host', parent=parent)) as current:
            self.DIGITS(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src='.', parent=current)
                    self.DIGITS(parent=current)
            return current
    v4host.min_depth = 1

    def v6host(self, parent=None):
        with RuleContext(self, UnparserRule(name='v6host', parent=parent)) as current:
            with AlternationContext(self, [0, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                src = ['::', None][choice0]
                rule = [None, self.HEXD][choice0]
                if src is not None:
                    UnlexerRule(src=src, parent=current)
                else:
                    rule(parent=current)
            return current
    v6host.min_depth = 0

    def port(self, parent=None):
        with RuleContext(self, UnparserRule(name='port', parent=parent)) as current:
            self.DIGITS(parent=current)
            return current
    port.min_depth = 1

    def path(self, parent=None):
        with RuleContext(self, UnparserRule(name='path', parent=parent)) as current:
            self.string(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src='/', parent=current)
                    self.string(parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    UnlexerRule(src='/', parent=current)
            return current
    path.min_depth = 2

    def user(self, parent=None):
        with RuleContext(self, UnparserRule(name='user', parent=parent)) as current:
            self.string(parent=current)
            return current
    user.min_depth = 2

    def login(self, parent=None):
        with RuleContext(self, UnparserRule(name='login', parent=parent)) as current:
            self.user(parent=current)
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    UnlexerRule(src=':', parent=current)
                    self.password(parent=current)
            UnlexerRule(src='@', parent=current)
            return current
    login.min_depth = 3

    def password(self, parent=None):
        with RuleContext(self, UnparserRule(name='password', parent=parent)) as current:
            self.string(parent=current)
            return current
    password.min_depth = 2

    def frag(self, parent=None):
        with RuleContext(self, UnparserRule(name='frag', parent=parent)) as current:
            UnlexerRule(src='#', parent=current)
            with AlternationContext(self, [2, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.string, self.DIGITS][choice0](parent=current)
            return current
    frag.min_depth = 1

    def query(self, parent=None):
        with RuleContext(self, UnparserRule(name='query', parent=parent)) as current:
            UnlexerRule(src='?', parent=current)
            self.search(parent=current)
            return current
    query.min_depth = 4

    def search(self, parent=None):
        with RuleContext(self, UnparserRule(name='search', parent=parent)) as current:
            self.searchparameter(parent=current)
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.DELIMITER(parent=current)
                    self.searchparameter(parent=current)
            return current
    search.min_depth = 3

    def searchparameter(self, parent=None):
        with RuleContext(self, UnparserRule(name='searchparameter', parent=parent)) as current:
            self.string(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    UnlexerRule(src='=', parent=current)
                    with AlternationContext(self, [2, 1, 1], [1, 1, 1]) as weights0:
                        choice0 = self._model.choice(current, 0, weights0)
                        [self.string, self.DIGITS, self.HEX][choice0](parent=current)
            return current
    searchparameter.min_depth = 2

    def string(self, parent=None):
        with RuleContext(self, UnparserRule(name='string', parent=parent)) as current:
            with AlternationContext(self, [1, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.STRING, self.DIGITS][choice0](parent=current)
            return current
    string.min_depth = 1

    def DIGITS(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DIGITS', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            return current
    DIGITS.min_depth = 0

    def STRING(self, parent=None):
        with RuleContext(self, UnlexerRule(name='STRING', parent=parent)) as current:
            with AlternationContext(self, [0, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[2]), parent=current)
                elif choice0 == 1:
                    self.HEX(parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    with AlternationContext(self, [0, 1], [1, 1]) as weights1:
                        choice1 = self._model.choice(current, 1, weights1)
                        if choice1 == 0:
                            UnlexerRule(src=self._model.charset(current, 1, self._charsets[3]), parent=current)
                        elif choice1 == 1:
                            self.HEX(parent=current)
            return current
    STRING.min_depth = 0

    def HEXD(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEXD', parent=parent)) as current:
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            UnlexerRule(src=':', parent=current)
            self.HEXUNIT(parent=current)
            return current
    HEXD.min_depth = 1

    def HEXUNIT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEXUNIT', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[4]), parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[5]), parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    UnlexerRule(src=self._model.charset(current, 2, self._charsets[6]), parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 2, min=0, max=1):
                    UnlexerRule(src=self._model.charset(current, 3, self._charsets[7]), parent=current)
            return current
    HEXUNIT.min_depth = 0

    def HEX(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEX', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    UnlexerRule(src='%', parent=current)
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[8]), parent=current)
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[9]), parent=current)
            return current
    HEX.min_depth = 0

    def DELIMITER(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DELIMITER', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['&', ';'][choice0], parent=current)
            return current
    DELIMITER.min_depth = 0

    def hostname_DomainNameOrIPv4Host(self, parent=None):
        with RuleContext(self, UnparserRule(name='hostname_DomainNameOrIPv4Host', parent=parent)) as current:
            self.string(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src='.', parent=current)
                    self.string(parent=current)
            return current
    hostname_DomainNameOrIPv4Host.min_depth = 2

    def hostname_IPv4Host(self, parent=None):
        with RuleContext(self, UnparserRule(name='hostname_IPv4Host', parent=parent)) as current:
            self.v4host(parent=current)
            return current
    hostname_IPv4Host.min_depth = 2

    def hostname_IPv6Host(self, parent=None):
        with RuleContext(self, UnparserRule(name='hostname_IPv6Host', parent=parent)) as current:
            UnlexerRule(src='[', parent=current)
            self.v6host(parent=current)
            UnlexerRule(src=']', parent=current)
            return current
    hostname_IPv6Host.min_depth = 1

    _default_rule = url

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(48, 58)])),
        2: list(itertools.chain.from_iterable([range(48, 58), range(65, 91), range(97, 123), range(126, 127)])),
        3: list(itertools.chain.from_iterable([range(43, 44), range(45, 46), range(48, 58), range(65, 91), range(97, 123)])),
        4: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        5: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        6: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        7: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        8: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
        9: list(itertools.chain.from_iterable([range(48, 58), range(65, 71), range(97, 103)])),
    }
