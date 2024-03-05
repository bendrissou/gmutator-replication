import sys
from antlr4 import *
from urlLexer import urlLexer
from urlParser import urlParser
#from MyErrorListener import MyErrorListener
import io

def main(argv):
    input = FileStream(argv[1], encoding = 'utf8')
    #print("\nInput is: " + str(input))
    lexer = urlLexer(input)
    #lexer.removeErrorListeners()
    #lexer.addErrorListener(MyErrorListener())  
    stream = CommonTokenStream(lexer)
    parser = urlParser(stream)

    try:
        tree = parser.url()
    except SyntaxError:
        print("\n ++++++ Syntax Error ++++++ \n")
    except Exception as e:
        print("\nInput is: " + str(input))
        print("Error is: " + str(e))
        print("\n ++++++ Other Error ++++++ \n")

if __name__ == '__main__':
    main(sys.argv)
