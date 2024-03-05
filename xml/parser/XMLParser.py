# Generated from XMLParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,3,0,18,8,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,0,1,0,
        5,0,28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,5,1,37,8,1,10,1,12,1,
        40,9,1,1,1,1,1,1,2,3,2,45,8,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,2,
        3,2,55,8,2,5,2,57,8,2,10,2,12,2,60,9,2,1,3,1,3,1,3,5,3,65,8,3,10,
        3,12,3,68,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,80,8,3,
        10,3,12,3,83,9,3,1,3,3,3,86,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,
        1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,3,1,0,4,5,2,0,6,6,9,9,3,0,
        1,1,6,6,18,18,103,0,17,1,0,0,0,2,34,1,0,0,0,4,44,1,0,0,0,6,85,1,
        0,0,0,8,87,1,0,0,0,10,89,1,0,0,0,12,93,1,0,0,0,14,95,1,0,0,0,16,
        18,3,2,1,0,17,16,1,0,0,0,17,18,1,0,0,0,18,22,1,0,0,0,19,21,3,14,
        7,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,
        1,0,0,0,24,22,1,0,0,0,25,29,3,6,3,0,26,28,3,14,7,0,27,26,1,0,0,0,
        28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,
        0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,38,5,8,0,0,35,37,3,10,5,0,36,
        35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,
        0,40,38,1,0,0,0,41,42,5,11,0,0,42,3,1,0,0,0,43,45,3,12,6,0,44,43,
        1,0,0,0,44,45,1,0,0,0,45,58,1,0,0,0,46,52,3,6,3,0,47,52,3,8,4,0,
        48,52,5,2,0,0,49,52,5,18,0,0,50,52,5,1,0,0,51,46,1,0,0,0,51,47,1,
        0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,54,1,0,0,0,53,
        55,3,12,6,0,54,53,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,51,1,0,
        0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,5,1,0,0,0,60,58,
        1,0,0,0,61,62,5,7,0,0,62,66,5,16,0,0,63,65,3,10,5,0,64,63,1,0,0,
        0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,
        1,0,0,0,69,70,5,10,0,0,70,71,3,4,2,0,71,72,5,7,0,0,72,73,5,13,0,
        0,73,74,5,16,0,0,74,75,5,10,0,0,75,86,1,0,0,0,76,77,5,7,0,0,77,81,
        5,16,0,0,78,80,3,10,5,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,
        0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,86,5,12,0,0,85,61,
        1,0,0,0,85,76,1,0,0,0,86,7,1,0,0,0,87,88,7,0,0,0,88,9,1,0,0,0,89,
        90,5,16,0,0,90,91,5,14,0,0,91,92,5,15,0,0,92,11,1,0,0,0,93,94,7,
        1,0,0,94,13,1,0,0,0,95,96,7,2,0,0,96,15,1,0,0,0,11,17,22,29,38,44,
        51,54,58,66,81,85
    ]

class XMLParser ( Parser ):

    grammarFileName = "XMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "<INVALID>", 
                     "<INVALID>", "'>'", "<INVALID>", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "CDATA", "DTD", "EntityRef", 
                      "CharRef", "SEA_WS", "OPEN", "XMLDeclOpen", "TEXT", 
                      "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", 
                      "EQUALS", "STRING", "Name", "S", "PI" ]

    RULE_document = 0
    RULE_prolog = 1
    RULE_content = 2
    RULE_element = 3
    RULE_reference = 4
    RULE_attribute = 5
    RULE_chardata = 6
    RULE_misc = 7

    ruleNames =  [ "document", "prolog", "content", "element", "reference", 
                   "attribute", "chardata", "misc" ]

    EOF = Token.EOF
    COMMENT=1
    CDATA=2
    DTD=3
    EntityRef=4
    CharRef=5
    SEA_WS=6
    OPEN=7
    XMLDeclOpen=8
    TEXT=9
    CLOSE=10
    SPECIAL_CLOSE=11
    SLASH_CLOSE=12
    SLASH=13
    EQUALS=14
    STRING=15
    Name=16
    S=17
    PI=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(XMLParser.ElementContext,0)


        def EOF(self):
            return self.getToken(XMLParser.EOF, 0)

        def prolog(self):
            return self.getTypedRuleContext(XMLParser.PrologContext,0)


        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = XMLParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 16
                self.prolog()


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262210) != 0):
                self.state = 19
                self.misc()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.element()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262210) != 0):
                self.state = 26
                self.misc()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(XMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrologContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XMLDeclOpen(self):
            return self.getToken(XMLParser.XMLDeclOpen, 0)

        def SPECIAL_CLOSE(self):
            return self.getToken(XMLParser.SPECIAL_CLOSE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_prolog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProlog" ):
                listener.enterProlog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProlog" ):
                listener.exitProlog(self)




    def prolog(self):

        localctx = XMLParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(XMLParser.XMLDeclOpen)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 35
                self.attribute()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(XMLParser.SPECIAL_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(XMLParser.ElementContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==9:
                self.state = 43
                self.chardata()


            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 51
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7]:
                        self.state = 46
                        self.element()
                        pass
                    elif token in [4, 5]:
                        self.state = 47
                        self.reference()
                        pass
                    elif token in [2]:
                        self.state = 48
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [18]:
                        self.state = 49
                        self.match(XMLParser.PI)
                        pass
                    elif token in [1]:
                        self.state = 50
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6 or _la==9:
                        self.state = 53
                        self.chardata()

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.OPEN)
            else:
                return self.getToken(XMLParser.OPEN, i)

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CLOSE)
            else:
                return self.getToken(XMLParser.CLOSE, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def SLASH(self):
            return self.getToken(XMLParser.SLASH, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def SLASH_CLOSE(self):
            return self.getToken(XMLParser.SLASH_CLOSE, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = XMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(XMLParser.OPEN)
                self.state = 62
                self.match(XMLParser.Name)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 63
                    self.attribute()
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                self.match(XMLParser.CLOSE)
                self.state = 70
                self.content()
                self.state = 71
                self.match(XMLParser.OPEN)
                self.state = 72
                self.match(XMLParser.SLASH)
                self.state = 73
                self.match(XMLParser.Name)
                self.state = 74
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(XMLParser.OPEN)
                self.state = 77
                self.match(XMLParser.Name)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 78
                    self.attribute()
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 84
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EntityRef(self):
            return self.getToken(XMLParser.EntityRef, 0)

        def CharRef(self):
            return self.getToken(XMLParser.CharRef, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)




    def reference(self):

        localctx = XMLParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XMLParser.Name, 0)

        def EQUALS(self):
            return self.getToken(XMLParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(XMLParser.Name)
            self.state = 90
            self.match(XMLParser.EQUALS)
            self.state = 91
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChardataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_chardata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChardata" ):
                listener.enterChardata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChardata" ):
                listener.exitChardata(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==6 or _la==9):
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


    class MiscContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(XMLParser.COMMENT, 0)

        def PI(self):
            return self.getToken(XMLParser.PI, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_misc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMisc" ):
                listener.enterMisc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMisc" ):
                listener.exitMisc(self)




    def misc(self):

        localctx = XMLParser.MiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 262210) != 0)):
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





