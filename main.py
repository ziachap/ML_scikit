"""Script to gather IMDB keywords from 2013's top grossing movies."""
import sys
import numpy as np
from sklearn import svm
from sklearn.metrics import f1_score

def main():
    """Main entry point for the script."""
    print("hello world")
    fh = open("hello.txt","r")
	print fh.read()
    pass

if __name__ == '__main__':
    sys.exit(main())