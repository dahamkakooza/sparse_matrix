import re

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                print("Lines read from file:")
                print(lines)  # Debug print the raw lines read from the file
                
                rows = int(re.search(r'\d+', lines[0]).group())
                cols = int(re.search(r'\d+', lines[1]).group())
                matrix = cls(rows, cols)

                for line in lines[2:]:
                    line = line.strip()  # Remove leading/trailing spaces and newlines
                    if line:  # Only process non-empty lines
                        print(f"Processing line: {line}")  # Debug print each line being processed
                        match = re.match(r'\((\d+),\s*(\d+),\s*(-?\d+)\)', line)
                        if match:
                            r, c, v = map(int, match.groups())
                            matrix.set_element(r, c, v)
                        else:
                            raise ValueError("Input file has wrong format")
                    else:
                        print("Skipping empty line")  # Debug: Show skipped empty line

                return matrix
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")

    def set_element(self, row, col, value):
        if row >= self.rows or col >= self.cols or row < 0 or col < 0:
            raise IndexError("Invalid index")
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"rows={self.rows}\n")
            file.write(f"cols={self.cols}\n")
            for (r, c), v in sorted(self.data.items()):
                file.write(f"({r}, {c}, {v})\n")

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition")
        result = SparseMatrix(self.rows, self.cols)
        for (r, c), v in {**self.data, **other.data}.items():
            result.set_element(r, c, self.get_element(r, c) + other.get_element(r, c))
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        result = SparseMatrix(self.rows, self.cols)
        for (r, c), v in {**self.data, **other.data}.items():
            result.set_element(r, c, self.get_element(r, c) - other.get_element(r, c))
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for (r1, c1), v1 in self.data.items():
            for c2 in range(other.cols):
                if (c1, c2) in other.data:
                    result.set_element(r1, c2, result.get_element(r1, c2) + v1 * other.data[(c1, c2)])
        return result

    def display(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.get_element(r, c), end=" ")
            print()

if __name__ == "__main__":
    try:
        A = SparseMatrix.from_file(r"C:\Users\HP\Documents\dsa\sparse_matrix\sample_inputs\matrix1.txt")
        B = SparseMatrix.from_file(r"C:\Users\HP\Documents\dsa\sparse_matrix\sample_inputs\matrix2.txt")

        print("Matrix A:")
        A.display()
        print("Matrix B:")
        B.display()
        
        C = A + B
        C.to_file(r"addition_results.txt")
        print("Addition Result written to addition_result.txt")
        
        D = A - B
        D.to_file(r"subtraction_results.txt")
        print("Subtraction Result written to subtraction_result.txt")
        
        E = A * B
        E.to_file(r"multiplication_results.txt")
        print("Multiplication Result written to multiplication_result.txt")
        
    except Exception as e:
        print(f"Error: {e}")
