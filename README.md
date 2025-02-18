# sparse_matrix
# Sparse Matrix Operations

## Overview
This project implements a **Sparse Matrix** using Python. It supports the following operations:
- **Addition**
- **Subtraction**
- **Multiplication**

The program reads sparse matrices from input files and writes results to output files.

## 🚀 How to Run the Program

```
- The first line specifies the **number of rows**.
- The second line specifies the **number of columns**.
- Each remaining line represents a **non-zero matrix element** in the format `(row, column, value)`.

Place your input files (`matrix1.txt`, `matrix2.txt`) in the `sample_inputs/` directory.

### **Step 2: Run the Program**
Navigate to the `/code/src/` directory and execute:
```sh
python sparse_matrix.py
```
The program will read `matrix1.txt` and `matrix2.txt`, perform operations, and generate output files.

### **Step 3: Check Output Files**
After execution, the results will be saved in:
- **addition_result.txt**  (Matrix A + B)
- **subtraction_result.txt**  (Matrix A - B)
- **multiplication_result.txt**  (Matrix A * B)

---

 ## Error Handling
- If an input file contains incorrect formatting, the program **raises an error**.
- The program ensures matrices have **compatible dimensions** before performing operations.



