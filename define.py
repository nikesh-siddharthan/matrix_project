def Matrix_create():
    matrix = ['Give proper order']
    order_of_matrix = int(input("Enter the order of the matrix (1-3): "))
    
    if 0 < order_of_matrix < 4:
        matrix = []
        for i in range(order_of_matrix):
            row = []
            for j in range(order_of_matrix):
                value = int(input(f"Enter the value for A[{i+1}][{j+1}]: "))
                row.append(value)
            matrix.append(row)
    return matrix

def double_matrix ():
    matrix1 = Matrix_create()
    matrix2 = Matrix_create()
    return [matrix1,matrix2]
print(Matrix_create())