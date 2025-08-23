from side_operation import matrix_to_list , list_to_matrix
def add (matrix_1 , matrix_2):
    list_matrix_1 = matrix_to_list(matrix_1)
    list_matrix_2 = matrix_to_list(matrix_2)
    modified_list = []
    for i in range(len(list_matrix_1)):
        modified_list.append(list_matrix_1[i]+list_matrix_2[i])
    return list_to_matrix(modified_list)

def sub (matrix_1 , matrix_2):
    list_matrix_1 = matrix_to_list(matrix_1)
    list_matrix_2 = matrix_to_list(matrix_2)
    modified_list = []
    for i in range(len(list_matrix_1)):
        modified_list.append(list_matrix_1[i]-list_matrix_2[i])
    return list_to_matrix(modified_list)

def determinant (matrix):
    print("")

def multiplication_matrix (matrix1,matrix2):
    matrix_2_transopose = transpose_matrix(matrix2)
    order = len(matrix2)
    for i in range(order*order):
        row = []
        count =0 
        for ele1 in matrix1:
            sum_matrix = []
            for element in ele1:
                sum_matrix.append(element*matrix_2_transopose[count])
                count +=1
            val = 0 
            for val in sum_matrix:
                value = value + val
                print("val :",val , 'value :', value)
            int_sum = int(sum_matrix)
            row.append(int_sum)
            print(int_sum)
def transpose_matrix (matrix):
    matrix_transpose = []
    order = len(matrix)
    for i in range(order) :
        row = []
        for j in range(order):
            row.append(matrix[j][i])
        matrix_transpose.append(row)
    return matrix_transpose


