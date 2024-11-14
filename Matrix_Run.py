from Matrix import Matrix
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