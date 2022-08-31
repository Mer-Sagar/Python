"""
12. Write a program to read a matrix and determine the following :
   (1) wheather the given matrix is upper triangular or not
   (2) wheather the given matrix is lower triangular or not
   (3) wheather the given matrix is digonal matrix or not

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""
import numpy as np
def matrix_print(mat, r):
    for i in range(r):
        for j in range(r):
            print(mat[i][j], end=" ")
        print()

def check_upper(mat, r):
    for i in range(1, r):
        for j in range(0, i):
            if mat[i][j] != 0:
                print("The Given matrix is not a upper triangular matrix")
                return
    print("The given matrix is upper triangular matrix")

def check_lower(mat, r):
    for i in range(0, r):
        for j in range(i+1, r):
            if mat[i][j] != 0:
                print("The given matrix is not a lower triangular matrix")
                return
    print("The given matrix is lower triangular matrix")

def check_diagonal(mat, r):
    for i in range(r):
        for j in range(r):
            if i!=j and mat[i][j] != 0:
                print("The given matrix is not a diagonal matrix")
                return
    print("The given matrix is diagonal matrix")


r = int(input("Enter the number of rows and cols : "))
lst1 = []

for i in range(r*r):
    item = int(input("Enter the item : "))
    lst1.append(item)

mat1 = np.array(lst1).reshape(r, r)

print("The given matrix is: ")
matrix_print(mat1, r)
check_upper(mat1, r)
check_lower(mat1, r)
check_diagonal(mat1, r)

