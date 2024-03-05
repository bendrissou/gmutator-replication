import sys
from antlr4 import *
from LuaLexer import LuaLexer
from LuaParser import LuaParser
#from MyErrorListener import MyErrorListener
import io

def main(argv):
    input = FileStream(argv[1], encoding = 'utf8')
    #print("\nInput is: " + str(input))
    lexer = LuaLexer(input)
    #lexer.removeErrorListeners()
    #lexer.addErrorListener(MyErrorListener())  
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)

    try:
        tree = parser.chunk()
    except SyntaxError:
        print("\n ++++++ Syntax Error ++++++ \n")
    except Exception as e:
        print("\nInput is: " + str(input))
        print("Error is: " + str(e))
        print("\n ++++++ Other Error ++++++ \n")

if __name__ == '__main__':
    main(sys.argv)
