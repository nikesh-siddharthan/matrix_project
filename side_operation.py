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



        

def order_check (matrix):
    return len(matrix) 

def matrix_print (matrix):
    for i in matrix :
        print(i)
