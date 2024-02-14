matrix1=[]
matrix2=[]
result=[]

def insert_in_matrix(matrix , row, col):
    for i in range(row):
        row=[]
        for j in range(col):
            a=int(input(f"enter the element to be appended for row {i} "))
            row.append(a)
        matrix.append(row)

def multiplication_matrix(matrix1,matrix2):
    result = []

    # Check if matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    # Initialize result matrix with zeros
    for i in range(len(matrix1)):
        result.append([0] * len(matrix2[0]))

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

insert_in_matrix(matrix1, 3, 3)
insert_in_matrix(matrix2, 3, 3)
print(matrix1)
print(matrix2)
result=multiplication_matrix(matrix1,matrix2)
print(result)