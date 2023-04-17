# Sparse matrix implemented with dictionary

# sparse matrix is a structure that only stores values that are present in the matrix

dim = 6, 12
mat = {}

#Tuples are immutable, each tuple represents a position in the matrix

mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9


for row in range(dim[0]):
    for col in range(dim[1]):
         print( mat.get((row, col), 0),)
    print('\n')
