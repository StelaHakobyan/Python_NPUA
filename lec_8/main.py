class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[(i + j) for j in range(m)] for i in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / (self.n * self.m)

    def sum_of_row(self, row_index):
        return sum(self.matrix[row_index])

    def average_of_column(self, col_index):
        total_sum = sum(row[col_index] for row in self.matrix)
        return total_sum / self.n

    def print_submatrix(self, col_range, row_range):
        submatrix = [row[col_range[0]:col_range[1]+1] for row in self.matrix[row_range[0]:row_range[1]+1]]
        for row in submatrix:
            print(row)


matrix = Matrix(3, 3)


print("Matrix:")
matrix.print_matrix()


mean = matrix.calculate_mean()
print(f"\nMean of the matrix: {mean}")


row_sum = matrix.sum_of_row(0)
print(f"Sum of the first row: {row_sum}")

col_average = matrix.average_of_column(1)
print(f"Average of the second column: {col_average}")


print("\nSubmatrix:")
matrix.print_submatrix([0, 1], [1, 2])
