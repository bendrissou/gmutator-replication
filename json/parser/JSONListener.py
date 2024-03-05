# Generated from JSON.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

# This class defines a complete listener for a parse tree produced by JSONParser.
class JSONListener(ParseTreeListener):

    # Enter a parse tree produced by JSONParser#json.
    def enterJson(self, ctx:JSONParser.JsonContext):
        pass

    # Exit a parse tree produced by JSONParser#json.
    def exitJson(self, ctx:JSONParser.JsonContext):
        pass


    # Enter a parse tree produced by JSONParser#obj.
    def enterObj(self, ctx:JSONParser.ObjContext):
        pass

    # Exit a parse tree produced by JSONParser#obj.
    def exitObj(self, ctx:JSONParser.ObjContext):
        pass


    # Enter a parse tree produced by JSONParser#pair.
    def enterPair(self, ctx:JSONParser.PairContext):
        pass

    # Exit a parse tree produced by JSONParser#pair.
    def exitPair(self, ctx:JSONParser.PairContext):
        pass


    # Enter a parse tree produced by JSONParser#arr.
    def enterArr(self, ctx:JSONParser.ArrContext):
        pass

    # Exit a parse tree produced by JSONParser#arr.
    def exitArr(self, ctx:JSONParser.ArrContext):
        pass


    # Enter a parse tree produced by JSONParser#value.
    def enterValue(self, ctx:JSONParser.ValueContext):
        pass

    # Exit a parse tree produced by JSONParser#value.
    def exitValue(self, ctx:JSONParser.ValueContext):
        pass



del JSONParser