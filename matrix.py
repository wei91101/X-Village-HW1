import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.a = []
        self.nrows = nrows
        self.ncols = ncols
        for i in range(self.nrows):
            b = []
            self.a.append(b)           
            for j in range(self.ncols):
                b.append(random.randint(0,9))  

    def add(self, m):
        """return a new Matrix object after summation"""
        matrix = Matrix(self.nrows,self.ncols)
        a = []
        self.matrix2 = m
        for i in range(self.nrows):
            b = []
            a.append(b)
            for j in range(self.ncols):
                #x = self.a[i][j] + self.matrix2[i][j]
                b.append(self.a[i][j] + self.matrix2[i][j])
                #print(x)
        self.a = a

        return matrix
        
    def sub(self, m):
        """return a new Matrix object after substraction"""
        matrix = Matrix(self.nrows,self.ncols)
        a = []
        self.matrix2 = m
        for i in range(self.nrows):
            b = []
            a.append(b)
            for j in range(self.ncols):
                x = self.a[i][j] - self.matrix2[i][j]
                b.append(self.a[i][j] - self.matrix2[i][j])
                #print(x)
        self.a = a
        return matrix

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        matrix = Matrix(self.nrows,self.ncols)
        self.matrix2 = m
        a = []
        self.mul_sum = []
        for i in range (len(self.a)):
            b = []
            a.append(b)
            for j in range (len(self.matrix2[0])):
                self.z = 0
                for k in range (len(self.a[0])):
                    self.z = self.z + self.a[i][k] * self.matrix2[k][j]
                    #print(z)
                b.append(self.z)
        self.a = a
        # print(self.mul_sum,end="")
        return matrix

                

    def transpose(self):
        """return a new Matrix object after transpose"""
        matrix = Matrix(self.nrows,self.ncols)
        a = []
        for i in range (len(self.a)):
            b = []
            a.append(b)
            for j in range (len(self.a[0])):
                b.append(self.a[j][i])
        self.a = a
        return matrix

    
    def display(self):
        """Display the content in the matrix"""
        for i in range (len(self.a)):
            for j in range (len(self.a[0])):
                print(self.a[i][j], end=" ")
            print("")
        print("")
        # print(len(self.a))
        # print(len(self.a[0]))
# nrows = 3
# ncols = 3
# b = []
# for i in range (nrows):
#     a = []
#     b.append(a)
#     #print(b)
#     for j in range (ncols):
#         a.append(random.randint(0,9))
#print(b)
# # print(b[2][1])
# y = []
# for i in range (nrows):
#     z = []
#     y.append(z)
#     for j in range(ncols):
#         x = b[i][j] + b[i][j]
#         print(x)
#         z.append(x)        

# print(y)

a1 = int(input("Enter A matrix's rows:" ))
b1 = int(input("Enter A matrix's cols:" ))
a2 = int(input("Enter B matrix's rows:" ))
b2 = int(input("Enter B matrix's cols:" ))
matrix1 = Matrix(a1,b1)
matrix2 = Matrix(a2,b2)
matrix1.display()
matrix2.display()
matrix1.add(matrix2.a)
print(type(matrix1.add(matrix2.a)))
matrix1.display()
matrix1.sub(matrix2.a)
matrix1.sub(matrix2.a)
matrix1.display()
matrix1.add(matrix2.a)
matrix1.mul(matrix2.a)
matrix1.display()
matrix1.transpose()
matrix1.display()
