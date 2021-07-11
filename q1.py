from scipy import linalg
import numpy as np

def function_1(i: int, j: int, k: int):
    E = [[1 if i_loop == j_loop else 0 for j_loop in range(3)] for i_loop in range(3)]
    for step in range(len(E)):
        E[i][step] = E[i][step] + k * E[j][step]
    return E


def matrix_mux(X, Y):
    result = [[0 for j in range(len(Y[0]))] for i in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result;


def function_2(A, i: int, j: int, k: int):
    if len(A) != 3 or len(A[0]) != 3 or len(A[1]) != 3 or len(A[2]) != 3:
        raise Exception("matrix must be 3x3")

    E = function_1(i, j, k)
    result = matrix_mux(E, A)
    return result


def function_3(A, i: int, k: int):
    return function_2(A, i, i, k - 1)

def permutation_matrix(i_pos:int,j_pos:int):
    matrix = [[1 if (i==j) else 0 for i in range(3)] for j in range(3)]
    matrix[i_pos][i_pos]=0
    matrix[j_pos][j_pos]=0
    matrix[i_pos][j_pos] = 1
    matrix[j_pos][i_pos] = 1
    return matrix;

def function_4(A,i,j):
    if len(A) != 3 or len(A[0]) != 3 or len(A[1]) != 3 or len(A[2]) != 3:
        raise Exception("matrix must be 3x3")
    return matrix_mux(permutation_matrix(i,j),A)


def gaussian(A,y):
    if len(A) != 3 or len(A[0]) != 3 or len(A[1]) != 3 or len(A[2]) != 3:
        raise Exception("matrix must be 3x3")
    if len(y) != 3 :
        raise Exception("result must be 3x1")
    result = [[A[i][j] for j in range(3)] for i in range(3)]
    y_help = [ y[i] for i in range(3)]

    for i in range(len(A)):
        if(result[i][i] == 0):
            for j in range(i+1,len(A)):
                if (result[j][i] != 0):
                    result = function_4(result, i, j)
                    y_help[i], y_help[j] = y_help[j], y_help[i]
                    break;

        if result[i][i] == 0 and i != len(A)-1:
            raise Exception("there is problem in input")

        for j in range(i+1,len(A)):
            y_help[j] = y_help[j] - y_help[i]*(result[j][i] / result[i][i])
            result = function_2(result,j,i,-1*( result[j][i] / result[i][i]  ))



    for i in range(len(A)-1,-1,-1):


        if(result[i][i] == 0):
            for j in  range(i-1,-1,-1):
                if (result[j][i] != 0):
                    result = function_4(result, i, j)
                    y_help[i], y_help[j] = y_help[j], y_help[i]
                    break;

        if result[i][i] == 0 and i != 0:
            raise Exception("there is problem in input")


        for j in range(i-1,-1,-1):

            y_help[j] = y_help[j] - y_help[i]*(result[j][i] / result[i][i])
            result = function_2(result,j,i,-1*( result[j][i] / result[i][i]  ))




    for i in range(len(result)):
        if(result[i][i] == 0):
            raise Exception("it can't be solve")
        y_help[i] = round(y_help[i]/result[i][i],6)
        result = function_3(result,i,1/result[i][i])
    return y_help;

print(gaussian([[1, 2, 3], [4, 3, 1], [7, 2, 5]], [14,13,26]))


a = np.array([[1, 2, 3], [4, 3, 1], [7, 2, 5]])
b = np.array([14,13,26])
x = linalg.solve(a, b)
print(x)

'''
my result and scipy.linalg.solve are the same
'''
#ramin rowshan 9732491
