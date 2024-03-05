# Generated from url.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import random

def serializedATN():
    return [
        4,1,20,133,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,1,3,1,41,8,1,
        1,1,1,1,1,1,3,1,46,8,1,1,1,1,1,3,1,50,8,1,3,1,52,8,1,1,1,3,1,55,
        8,1,1,1,3,1,58,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,70,
        8,4,1,5,1,5,1,5,5,5,75,8,5,10,5,12,5,78,9,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,5,8,87,8,8,10,8,12,8,90,9,8,1,8,3,8,93,8,8,1,9,1,9,1,10,
        1,10,1,10,3,10,100,8,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,3,12,
        109,8,12,1,13,1,13,1,13,1,14,1,14,1,14,5,14,117,8,14,10,14,12,14,
        120,9,14,1,15,1,15,1,15,1,15,1,15,3,15,127,8,15,3,15,129,8,15,1,
        16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        0,3,1,0,4,6,2,0,10,10,17,17,1,0,15,16,132,0,34,1,0,0,0,2,37,1,0,
        0,0,4,59,1,0,0,0,6,61,1,0,0,0,8,69,1,0,0,0,10,71,1,0,0,0,12,79,1,
        0,0,0,14,81,1,0,0,0,16,83,1,0,0,0,18,94,1,0,0,0,20,96,1,0,0,0,22,
        103,1,0,0,0,24,105,1,0,0,0,26,110,1,0,0,0,28,113,1,0,0,0,30,121,
        1,0,0,0,32,130,1,0,0,0,34,35,3,2,1,0,35,36,5,0,0,1,36,1,1,0,0,0,
        37,38,3,4,2,0,38,40,5,1,0,0,39,41,3,20,10,0,40,39,1,0,0,0,40,41,
        1,0,0,0,41,42,1,0,0,0,42,45,3,6,3,0,43,44,5,2,0,0,44,46,3,14,7,0,
        45,43,1,0,0,0,45,46,1,0,0,0,46,51,1,0,0,0,47,49,5,3,0,0,48,50,3,
        16,8,0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,47,1,0,0,0,51,
        52,1,0,0,0,52,54,1,0,0,0,53,55,3,26,13,0,54,53,1,0,0,0,54,55,1,0,
        0,0,55,57,1,0,0,0,56,58,3,24,12,0,57,56,1,0,0,0,57,58,1,0,0,0,58,
        3,1,0,0,0,59,60,7,0,0,0,60,5,1,0,0,0,61,62,3,8,4,0,62,7,1,0,0,0,
        63,70,3,32,16,0,64,70,3,10,5,0,65,66,5,7,0,0,66,67,3,12,6,0,67,68,
        5,8,0,0,68,70,1,0,0,0,69,63,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,
        70,9,1,0,0,0,71,76,5,15,0,0,72,73,5,9,0,0,73,75,5,15,0,0,74,72,1,
        0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,11,1,0,0,0,78,
        76,1,0,0,0,79,80,7,1,0,0,80,13,1,0,0,0,81,82,5,15,0,0,82,15,1,0,
        0,0,83,88,3,32,16,0,84,85,5,3,0,0,85,87,3,32,16,0,86,84,1,0,0,0,
        87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,92,1,0,0,0,90,88,1,
        0,0,0,91,93,5,3,0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,17,1,0,0,0,94,
        95,3,32,16,0,95,19,1,0,0,0,96,99,3,18,9,0,97,98,5,2,0,0,98,100,3,
        22,11,0,99,97,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,102,5,11,
        0,0,102,21,1,0,0,0,103,104,3,32,16,0,104,23,1,0,0,0,105,108,5,12,
        0,0,106,109,3,32,16,0,107,109,5,15,0,0,108,106,1,0,0,0,108,107,1,
        0,0,0,109,25,1,0,0,0,110,111,5,13,0,0,111,112,3,28,14,0,112,27,1,
        0,0,0,113,118,3,30,15,0,114,115,5,20,0,0,115,117,3,30,15,0,116,114,
        1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,29,1,
        0,0,0,120,118,1,0,0,0,121,128,3,32,16,0,122,126,5,14,0,0,123,127,
        3,32,16,0,124,127,5,15,0,0,125,127,5,19,0,0,126,123,1,0,0,0,126,
        124,1,0,0,0,126,125,1,0,0,0,127,129,1,0,0,0,128,122,1,0,0,0,128,
        129,1,0,0,0,129,31,1,0,0,0,130,131,7,2,0,0,131,33,1,0,0,0,15,40,
        45,49,51,54,57,69,76,88,92,99,108,118,126,128
    ]

class urlParser ( Parser ):

    grammarFileName = "url.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'://'", "':'", "'/'", "'ftp'", "'http'", 
                     "'https'", "'['", "']'", "'.'", "'::'", "'@'", "'#'", 
                     "'?'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DIGITS", "STRING", 
                      "HEXD", "HEXUNIT", "HEX", "DELIMITER" ]

    RULE_url = 0
    RULE_uri = 1
    RULE_scheme = 2
    RULE_host = 3
    RULE_hostname = 4
    RULE_v4host = 5
    RULE_v6host = 6
    RULE_port = 7
    RULE_path = 8
    RULE_user = 9
    RULE_login = 10
    RULE_password = 11
    RULE_frag = 12
    RULE_query = 13
    RULE_search = 14
    RULE_searchparameter = 15
    RULE_string = 16

    ruleNames =  [ "url", "uri", "scheme", "host", "hostname", "v4host", 
                   "v6host", "port", "path", "user", "login", "password", 
                   "frag", "query", "search", "searchparameter", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    DIGITS=15
    STRING=16
    HEXD=17
    HEXUNIT=18
    HEX=19
    DELIMITER=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uri(self):
            return self.getTypedRuleContext(urlParser.UriContext,0)


        def EOF(self):
            return self.getToken(urlParser.EOF, 0)

        def getRuleIndex(self):
            return urlParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)




    def url(self):

        localctx = urlParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.uri()
            self.state = 35
            self.match(urlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UriContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scheme(self):
            return self.getTypedRuleContext(urlParser.SchemeContext,0)


        def host(self):
            return self.getTypedRuleContext(urlParser.HostContext,0)


        def login(self):
            return self.getTypedRuleContext(urlParser.LoginContext,0)


        def port(self):
            return self.getTypedRuleContext(urlParser.PortContext,0)


        def query(self):
            return self.getTypedRuleContext(urlParser.QueryContext,0)


        def frag(self):
            return self.getTypedRuleContext(urlParser.FragContext,0)


        def path(self):
            return self.getTypedRuleContext(urlParser.PathContext,0)


        def getRuleIndex(self):
            return urlParser.RULE_uri

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUri" ):
                listener.enterUri(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUri" ):
                listener.exitUri(self)




    def uri(self):

        localctx = urlParser.UriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_uri)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.scheme()
            self.state = 38
            self.match(urlParser.T__0)
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 39
                self.login()


            self.state = 42
            self.host()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 43
                self.match(urlParser.T__1)
                self.state = 44
                self.port()


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 47
                self.match(urlParser.T__2)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==16:
                    self.state = 48
                    self.path()




            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 53
                self.query()


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 56
                self.frag()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return urlParser.RULE_scheme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScheme" ):
                listener.enterScheme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScheme" ):
                listener.exitScheme(self)




    def scheme(self):

        localctx = urlParser.SchemeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_scheme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hostname(self):
            return self.getTypedRuleContext(urlParser.HostnameContext,0)


        def getRuleIndex(self):
            return urlParser.RULE_host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHost" ):
                listener.enterHost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHost" ):
                listener.exitHost(self)




    def host(self):

        localctx = urlParser.HostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_host)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.hostname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HostnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return urlParser.RULE_hostname

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IPv6HostContext(HostnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a urlParser.HostnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def v6host(self):
            return self.getTypedRuleContext(urlParser.V6hostContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIPv6Host" ):
                listener.enterIPv6Host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIPv6Host" ):
                listener.exitIPv6Host(self)


    class IPv4HostContext(HostnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a urlParser.HostnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def v4host(self):
            return self.getTypedRuleContext(urlParser.V4hostContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIPv4Host" ):
                listener.enterIPv4Host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIPv4Host" ):
                listener.exitIPv4Host(self)


    class DomainNameOrIPv4HostContext(HostnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a urlParser.HostnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(urlParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomainNameOrIPv4Host" ):
                listener.enterDomainNameOrIPv4Host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomainNameOrIPv4Host" ):
                listener.exitDomainNameOrIPv4Host(self)



    def hostname(self):

        localctx = urlParser.HostnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_hostname)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = urlParser.DomainNameOrIPv4HostContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.string()
                pass

            elif la_ == 2:
                localctx = urlParser.IPv4HostContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.v4host()
                pass

            elif la_ == 3:
                localctx = urlParser.IPv6HostContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(urlParser.T__6)
                self.state = 66
                self.v6host()
                self.state = 67
                self.match(urlParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V4hostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(urlParser.DIGITS)
            else:
                return self.getToken(urlParser.DIGITS, i)

        def getRuleIndex(self):
            return urlParser.RULE_v4host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV4host" ):
                listener.enterV4host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV4host" ):
                listener.exitV4host(self)




    def v4host(self):

        localctx = urlParser.V4hostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_v4host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(urlParser.DIGITS)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 72
                self.match(urlParser.T__8)
                self.state = 73
                self.match(urlParser.DIGITS)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V6hostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEXD(self):
            return self.getToken(urlParser.HEXD, 0)

        def getRuleIndex(self):
            return urlParser.RULE_v6host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV6host" ):
                listener.enterV6host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV6host" ):
                listener.exitV6host(self)




    def v6host(self):

        localctx = urlParser.V6hostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_v6host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==10 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(urlParser.DIGITS, 0)

        def getRuleIndex(self):
            return urlParser.RULE_port

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort" ):
                listener.enterPort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort" ):
                listener.exitPort(self)




    def port(self):

        localctx = urlParser.PortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_port)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(urlParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(urlParser.StringContext)
            else:
                return self.getTypedRuleContext(urlParser.StringContext,i)


        def getRuleIndex(self):
            return urlParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)




    def path(self):

        localctx = urlParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.string()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self.match(urlParser.T__2)
                    self.state = 85
                    self.string() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 91
                self.match(urlParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UserContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(urlParser.StringContext,0)


        def getRuleIndex(self):
            return urlParser.RULE_user

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUser" ):
                listener.enterUser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUser" ):
                listener.exitUser(self)




    def user(self):

        localctx = urlParser.UserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_user)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoginContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def user(self):
            return self.getTypedRuleContext(urlParser.UserContext,0)


        def password(self):
            return self.getTypedRuleContext(urlParser.PasswordContext,0)


        def getRuleIndex(self):
            return urlParser.RULE_login

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogin" ):
                listener.enterLogin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogin" ):
                listener.exitLogin(self)




    def login(self):

        localctx = urlParser.LoginContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_login)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.user()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 97
                self.match(urlParser.T__1)
                self.state = 98
                self.password()


            self.state = 101
            self.match(urlParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasswordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(urlParser.StringContext,0)


        def getRuleIndex(self):
            return urlParser.RULE_password

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassword" ):
                listener.enterPassword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassword" ):
                listener.exitPassword(self)




    def password(self):

        localctx = urlParser.PasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_password)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(urlParser.StringContext,0)


        def DIGITS(self):
            return self.getToken(urlParser.DIGITS, 0)

        def getRuleIndex(self):
            return urlParser.RULE_frag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrag" ):
                listener.enterFrag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrag" ):
                listener.exitFrag(self)




    def frag(self):

        localctx = urlParser.FragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_frag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(urlParser.T__11)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 106
                self.string()
                pass

            elif la_ == 2:
                self.state = 107
                self.match(urlParser.DIGITS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def search(self):
            return self.getTypedRuleContext(urlParser.SearchContext,0)


        def getRuleIndex(self):
            return urlParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = urlParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(urlParser.T__12)
            self.state = 111
            self.search()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def searchparameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(urlParser.SearchparameterContext)
            else:
                return self.getTypedRuleContext(urlParser.SearchparameterContext,i)


        def DELIMITER(self, i:int=None):
            if i is None:
                return self.getTokens(urlParser.DELIMITER)
            else:
                return self.getToken(urlParser.DELIMITER, i)

        def getRuleIndex(self):
            return urlParser.RULE_search

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearch" ):
                listener.enterSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearch" ):
                listener.exitSearch(self)




    def search(self):

        localctx = urlParser.SearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_search)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.searchparameter()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 114
                self.match(urlParser.DELIMITER)
                self.state = 115
                self.searchparameter()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchparameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(urlParser.StringContext)
            else:
                return self.getTypedRuleContext(urlParser.StringContext,i)


        def DIGITS(self):
            return self.getToken(urlParser.DIGITS, 0)

        def HEX(self):
            return self.getToken(urlParser.HEX, 0)

        def getRuleIndex(self):
            return urlParser.RULE_searchparameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchparameter" ):
                listener.enterSearchparameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchparameter" ):
                listener.exitSearchparameter(self)




    def searchparameter(self):

        localctx = urlParser.SearchparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_searchparameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.string()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 122
                self.match(urlParser.T__13)
                self.state = 126
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 123
                    self.string()
                    pass

                elif la_ == 2:
                    self.state = 124
                    self.match(urlParser.DIGITS)
                    pass

                elif la_ == 3:
                    self.state = 125
                    self.match(urlParser.HEX)
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(urlParser.STRING, 0)

        def DIGITS(self):
            return self.getToken(urlParser.DIGITS, 0)

        def getRuleIndex(self):
            return urlParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = urlParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





