from side_operation import matrix_to_list , list_to_matrix
def add (matrix_1 , matrix_2):
    list_matrix_1 = matrix_to_list()
    list_matrix_2 = matrix_to_list()
    modified_list = []
    for i in range(len(list_matrix_1)):
        modified_list.append(list_matrix_1[i]+list_matrix_2[i])
    return list_to_matrix(modified_list)

def sub (matrix_1 , matrix_2):
    list_matrix_1 = matrix_to_list()
    list_matrix_2 = matrix_to_list()
    modified_list = []
    for i in range(len(list_matrix_1)):
        modified_list.append(list_matrix_1[i]-list_matrix_2[i])
    return list_to_matrix(modified_list)

def determinant (matrix):
    print("")

def multiplication_matrix (matrix1,matrix2):
    matrix1_list = matrix_to_list(matrix1)
    matrix2_list = matrix_to_list(matrix2)

def transpose_matrix (matrix):
    matrix_transpose = []
    order = len(matrix)
    for i in range(order) :
        row = []
        for j in range(order):
            print(matrix[j][i])
            row.append(matrix[j][i])
        matrix_transpose.append(row)
    return matrix_transpose

def matrix_print (matrix):
    for i in matrix :
        print(i)
        
matrix_print([[1, 4, 6], [9, 0, 4], [6, 3, 6]])