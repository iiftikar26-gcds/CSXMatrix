#Name: Irhan Iftikar
#Date: November 2024
#Description: CSX Assignment - Matrices

#Defines Matrix class and imports sys
import sys
class Matrix:
    #Function that initializes row, column, and data values for the matrix while asking user for matrix dimensions
    def __init__(self):
        while True:
            try:
                rows = int(input("Enter number of rows for your matrix: "))
                cols = int(input("Enter number of columns for your matrix: "))
                if rows <= 0 or cols <= 0:
                    print("Invalid input. You must enter a positive integer for both rows and columns.")
                    continue
                break
            except ValueError:
                print("Invalid input. You must enter a positive integer for both rows and columns.")
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    #Function that displays the menu options for the user to select
    def menu(self):
        print('''
    Matrix Calculation Options:
    -------------------------------------------------------------
    1 - Print the Matrices
    2 - Add the Matrices
    3 - Multiply the Matrices
    4 - Multiply a Row by a Scalar
    5 - Switch Rows of Matrix
    6 - Add Scalar times Row to another Row
    7 - Row Reduction of Matrix
    8 - Inverse of Matrix
    9 - Quit Program''')  

    #Function that takes user option from menu and calls on other functions within the Matrix class
    def operate(self, matrix2):
        choice = input("\nSelect an option from the menu (numbers 1-9): ") 
        if choice == "1":
            print("Matrix 1 (Trixie): ")
            self.print()
            print("Matrix 2 (Alice): ")
            matrix2.print()
        elif choice == "2":
            self.plus(matrix2)
        elif choice == "3":
            self.times(matrix2)
        elif choice == "4":
            scalar = float(input("Enter a scalar value: "))
            row = int(input("Enter the row number to be multipled: "))
            matrix_number = int(input("Which matrix do you want to modify? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.scalarTimesRow(scalar, row)
        elif choice == "5":
            row1 = int(input("Enter the first row to be switched: "))
            row2 = int(input("Enter the second row to be switched: "))
            matrix_number = int(input("Which matrix do you want to modify? (1 or 2)"))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.switchRows(row1, row2)
        elif choice == "6":
            scalar = float(input("Enter a scalar value: "))
            row1 = int(input("Enter the row number to be multipled by the scalar: "))
            row2 = int(input(f"Enter the row number to be modified by the scalar times row {row1}: "))
            matrix_number = int(input("Which matrix do you want to modify? (1 or 2)"))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.linearCombRows(scalar, row1, row2)
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            sys.exit(0)
        else:
            print("Option choice not valid, try again.")

    #Function that has the user create the matrix by entering values at each position
    def initialize_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                while True:
                    try:
                        self.data[i][j] = float(input(f"Enter a value at row {i+1}, column {j+1}: "))
                        break
                    except ValueError:
                        print("User didn't enter a numerical value. Try again.")
    
    #Function that prints the matrix to the user
    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end=" ")
            print()
        print("\n")
 
    #Function that finds the sum of two matrices
    def plus(self, matrix2):
        if self.rows != matrix2.rows or self.cols != matrix2.cols:
            print("Matrices cannot be added as they have different dimensions.\n")
            return None
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + matrix2.data[i][j]
        print("Sum of Matrices: ")
        for row in result:
            print(row)
        print("\n")

    #Function that finds the product of two matrices
    def times(self, matrix2):
        if self.cols != matrix2.rows:
            print("Matrices cannot be multipled as columns in the first matrix is not equal to rows in the second matrix.")
            return None
        result = [[0 for _ in range(self.rows)] for _ in range(matrix2.cols)]
        print("Product of Matrices: ")
        for i in range(self.rows):
            for j in range(matrix2.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * matrix2.data[k][j]
                print(result[i][j], end = " ")
            print()
        print("\n")

    #Function that multiples a row in the matrix by a scalar value
    def scalarTimesRow(self, scalar, row):
        row -= 1
        if 0 <= row < self.rows:
            for col in range(self.cols):
                self.data[row][col] *= scalar
        else:
            print("The entered row doesn't exist in the matrix.")
            return None
        print(f"Matrix result of scalar value {scalar} times row {row + 1}:")
        self.print()
        print("\n")

    #Function that switches two rows in a matrix
    def switchRows(self, firstrow, secondrow):
        firstrow -= 1
        secondrow -=1
        if 0 <= firstrow < self.rows and 0 <= secondrow < self.rows:
            self.data[firstrow], self.data[secondrow] = self.data[secondrow], self.data[firstrow]
            print(f"Matrix result of switching rows {firstrow + 1} and {secondrow + 1}:")
            self.print()
        else:
            print("The entered row(s) don't exist in the matrix.")
        print("\n")
    
    #Function that multiples a row by a scalar and adds it to another row
    def linearCombRows(self, scalar, firstrow, secondrow):
        firstrow -= 1
        secondrow -= 1
        if 0 <= firstrow < self.rows and 0 <= secondrow < self.rows:
            for i in range(self.cols):
                self.data[secondrow][i] += scalar * self.data[firstrow][i]
            print(f"Matrix result of multiplying row {firstrow + 1} by scalar {scalar} and adding to row {secondrow + 1}:")
            self.print()
        else:
            print("The entered row(s) don't exist in the matrix.")
        print("\n")
        
    def rowreduce(self):
        pass

    def invert(self):
        pass
    
if __name__ == "__main__":
    print("Dimensions for Matrix 1: ")
    trixie = Matrix()
    print("Dimensions for Matrix 2: ")
    alice = Matrix()
    print("Enter values for Matrix 1: ")
    trixie.initialize_matrix()
    print("\nEnter values for Matrix 2: ")
    alice.initialize_matrix()
    trixie.menu()
    while True:
        try:
            trixie.operate(alice)
        except ValueError:
            print("Invalid entry. Try again.")