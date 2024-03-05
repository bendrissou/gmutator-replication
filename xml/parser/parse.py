import sys
from antlr4 import *
from XMLLexer import XMLLexer
from XMLParser import XMLParser
#from MyErrorListener import MyErrorListener
import io

def main(argv):
    input = FileStream(argv[1], encoding = 'utf8')
    #print("\nInput is: " + str(input))
    lexer = XMLLexer(input)
    #lexer.removeErrorListeners()
    #lexer.addErrorListener(MyErrorListener())  
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)

    try:
        tree = parser.document()
    except SyntaxError:
        print("\n ++++++ Syntax Error ++++++ \n")
    except Exception as e:
        print("\nInput is: " + str(input))
        print("Error is: " + str(e))
        print("\n ++++++ Other Error ++++++ \n")

if __name__ == '__main__':
    main(sys.argv)
