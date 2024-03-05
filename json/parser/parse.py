import sys
from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
#from MyErrorListener import MyErrorListener
import io

def main(argv):
    input = FileStream(argv[1], encoding = 'utf8')
    #print("\nInput is: " + str(input))
    lexer = JSONLexer(input)
    #lexer.removeErrorListeners()
    #lexer.addErrorListener(MyErrorListener())  
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)

    try:
        tree = parser.json()
    except SyntaxError:
        print("\n ++++++ Syntax Error ++++++ \n")
    except Exception as e:
        print("\nInput is: " + str(input))
        print("Error is: " + str(e))
        print("\n ++++++ Other Error ++++++ \n")

if __name__ == '__main__':
    main(sys.argv)
