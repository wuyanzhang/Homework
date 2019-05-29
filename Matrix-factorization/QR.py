#coding:utf8
import numpy as np
from Print import Print
if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    A = np.array([[2., 2., 3.],
                  [4., 7., 7.],
                  [-2.,4., 5.]],dtype=float)
    print("=======Matrix factorization========")
    _str = str(input("Please Select Decomposition Type(LU GS HH or GV):"))
    control = "N"
    while control == 'N':
        try:
            if _str == 'LU':
                Print.printLU(A)
            elif _str == 'GS':
                Print.printGram_schmidt(A)
            elif _str == 'HH':
                Print.printHouseholder(A)
            elif _str == 'GV':
                Print.printGivens(A)
        except ValueError:
            print("Input is illegal")
        control = input("EXIT(Y/N)？")
