class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for col in range(cols)] for row in range(rows)]

    def __str__(self):
        string = ""
        for row in range(self.rows):
            for col in range(self.cols):
                string += str(self.matrix[row][col]) + " "
            string += "\n"
        return string

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be added")
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be subtracted")
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.matrix[row][col] = self.matrix[row][col] - other.matrix[row][col]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
        result = Matrix(self.rows, other.cols)
        for row in range(self.rows):
            for col in range(other.cols):
                for i in range(self.cols):
                    result.matrix[row][col] += self.matrix[row][i] * other.matrix[i][col]
        return result




m1 = Matrix(2, 2)
m1.matrix = [[1, 2], [3, 4]]

m2 = Matrix(2, 2)
m2.matrix = [[5, 6], [7, 8]]


m3 = m1 + m2
print(m3)


m4 = m1 - m2
print(m4)


m5 = m1 * m2
print(m5)