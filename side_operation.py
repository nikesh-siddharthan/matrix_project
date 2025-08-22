def matrix_to_list (matrix):
    list_of_matrix = []
    for row in matrix :
        for element in row :
            list_of_matrix.append(element)
    return list_of_matrix
def list_to_matrix_2 (list_matrix):
    matrix = []
    matrix.append([list_matrix[0],list_matrix[1]])    
    matrix.append([list_matrix[2],list_matrix[3]])
    return matrix 
def list_to_matrix_3(list_matrix):
    matrix = []
    matrix.append([list_matrix[0],list_matrix[1],list_matrix[2]])    
    matrix.append([list_matrix[3],list_matrix[4],list_matrix[5]])
    matrix.append([list_matrix[6],list_matrix[7],list_matrix[8]])
    return matrix
         
def list_to_matrix(list_matrix):
    order = order_check(list_matrix)
    if order == 4:
        return(list_to_matrix_2(list_matrix))
    if order == 9 :
        return(list_to_matrix_3(list_matrix)) 
    else :
        raise Exception ('Your list can not be modified to matrix')
    
        
def row_to_coloumn_convertor_3 (matrix):
    list_matrix = matrix_to_list(matrix)
    list_change_matrix = []
    count = -3
    count_2 = 0
    for i in range(3) :
        row_tO_coulum = []
        count_2 = count_2 + 1
        for j in range(3) :
            count = count + 3
            print(count)
            row_tO_coulum.append(list_matrix[count])
        count = count_2
        list_change_matrix.append(row_tO_coulum)
    return list_change_matrix
print(row_to_coloumn_convertor_3([[1, 4, 6], [9, 0, 4], [6, 3, 6]]))
        

def order_check (matrix):
    return len(matrix) 

