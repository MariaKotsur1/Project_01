import pprint

class Matrix:
    def __init__(self, row, colum):
        self.matrix = self.get_matrix(row, colum)

    def get_matrix(self, row, colum):
        num = 1
        matrix = [[None for j in range(colum)] for i in range(row)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 2
        return matrix
    
    def get_matrix_str(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)
    
    def __str__(self):
        return self.get_matrix_str(self.matrix)
    
    def __len__(self):
        return len(self.matrix)
    
    def add(self, matrix):
        self.content.append(matrix)

    def get_rows_count(self):
        return self.row 
    
    def get_colums_count(self):
        return self.colum
    
m = Matrix(5, 5)
print(m)
pprint.pprint(m)






    
 

    




