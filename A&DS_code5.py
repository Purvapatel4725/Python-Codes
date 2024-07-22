#Assignment-2 #Question-3
class Matrix:
    def __init__(self, rows, columns):
        # Initialize the Matrix object with the given number of rows and columns
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        # Return a string representation of the matrix
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __getitem__(self, index):
        # Get the value at the specified index in the matrix
        return self.data[index]

    def __setitem__(self, index, value):
        # Set the value at the specified index in the matrix
        self.data[index] = value

    def __add__(self, other):
        # Perform matrix addition with another matrix
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            # Check if the other object is a Matrix and has compatible dimensions
            result = Matrix(self.rows, self.columns)
            # Create a new Matrix object to store the result
            for i in range(self.rows):
                for j in range(self.columns):
                    # Add corresponding elements from self and other matrices
                    result[i][j] = self[i][j] + other[i][j]
            return result
        else:
            raise ValueError("Cannot perform matrix addition due to incompatible dimensions.")

    def __mul__(self, other):
        # Perform matrix multiplication with another matrix
        if isinstance(other, Matrix) and self.columns == other.rows:
            # Check if the other object is a Matrix and has compatible dimensions for multiplication
            result = Matrix(self.rows, other.columns)
            # Create a new Matrix object to store the result
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        # Perform the dot product of corresponding row and column elements
                        result[i][j] += self[i][k] * other[k][j]
            return result
        else:
            raise ValueError("Cannot perform matrix multiplication due to incompatible dimensions.")

# Function to read matrix elements from user input
def read_matrix(rows, columns):
    # Create a new Matrix object with the given number of rows and columns
    matrix = Matrix(rows, columns)
    for i in range(rows):
        while True:
            try:
                # Prompt the user to enter space-separated elements for the current row
                row_input = input(f"Enter space-separated elements for row {i+1}: ")
                # Split the input by spaces and convert the elements to integers
                elements = list(map(int, row_input.split()))
                if len(elements) != columns:
                    # Check if the number of entered elements matches the specified number of columns
                    raise ValueError("Invalid number of elements for the row.")
                # Assign the elements to the current row of the matrix
                matrix[i] = elements
                break
            except ValueError as e:
                # Handle the case when the user enters an invalid number of elements
                print(f"Error: {e} Please enter {columns} space-separated elements.")

    return matrix


# Create matrices
while True:
    try:
        # Prompt the user to enter the number of rows and columns for the first matrix
        m1_rows = int(input("Enter the number of rows for the first matrix: "))
        m1_columns = int(input("Enter the number of columns for the first matrix: "))
        # Call the read_matrix function to read the elements of the first matrix
        m1 = read_matrix(m1_rows, m1_columns)
        break
    except ValueError as e:
        # Handle the case when the user enters invalid dimensions
        print(f"Error: {e} Please enter valid dimensions.")

while True:
    try:
        # Prompt the user to enter the number of rows and columns for the second matrix
        m2_rows = int(input("Enter the number of rows for the second matrix: "))
        m2_columns = int(input("Enter the number of columns for the second matrix: "))
        # Call the read_matrix function to read the elements of the second matrix
        m2 = read_matrix(m2_rows, m2_columns)
        break
    except ValueError as e:
        # Handle the case when the user enters invalid dimensions
        print(f"Error: {e} Please enter valid dimensions.")

# Addition
try:
    # Perform matrix addition and store the result in the addition_result variable
    addition_result = m1 + m2
    print("Addition:")
    print(addition_result)
except ValueError as e:
    # Handle the case when the matrices cannot be added due to incompatible dimensions
    print(e)

# Multiplication
try:
    # Perform matrix multiplication and store the result in the multiplication_result variable
    multiplication_result = m1 * m2
    print("Multiplication:")
    print(multiplication_result)
except ValueError as e:
    # Handle the case when the matrices cannot be multiplied due to incompatible dimensions
    print(e)
