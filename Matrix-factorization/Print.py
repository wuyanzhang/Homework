import numpy as np
import Gram_schmidt
import Householder
import Givens
import LU
class Print:
    def printGram_schmidt(A):
        (Q, R) = Gram_schmidt.gram_schmidt(A)
        print("The Grimm Schmidt orthogonalization of the matrix is as follows:")
        print(Q)
        print(R)
        print(np.dot(Q,R))

    def printGivens(A):
        print("The Givens orthogonalization of the matrix is as follows:")
        (Q, R) = Givens.givens_rotation(A)
        print(Q)
        print(R)
        print(np.dot(Q,R))

    def printHouseholder(A):
        print("The Householder orthogonalization of the matrix is as follows:")
        (Q, R) = Householder.householder_reflection(A)
        print(Q)
        print(R)
        print(np.dot(Q,R))

    def printLU(A):
        print("The LU orthogonalization of the matrix is as follows:")
        (Q, R) = LU.LU_reflection(A)
        print(Q)
        print(R)
        print(np.dot(Q,R))