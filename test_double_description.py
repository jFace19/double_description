'''
Created on 09.12.2015

@author: lovis
'''
import unittest
import double_description
import numpy as np
from test.test_richcmp import Vector

class Test(unittest.TestCase):


    def test_Crosspolytope(self):
        file = open("crosspolytope.poly", "r")
        #first_line = data.readline()
        first_line = file.readline()
        m,d = first_line.split()
        m = int(m)
        d = int(d)
        liste = file.readlines()
        arraylist=[]
        for line in liste:
            a=[int(i) for i in line.split()]
            a=np.array(a)
            arraylist.append(a)
        matrix=np.matrix(arraylist)
        #double_description.double_description(matrix, m, d)
        pass
    
#     def test_Cube(self):
#         file = open("cube.poly", "r")
#         #first_line = data.readline()
#         first_line = file.readline()
#         m,d = first_line.split()
#         print("Dimension: ",d)
#         liste = file.readlines()
#         arraylist=[]
#         for line in liste:
#             a=[int(i) for i in line.split()]
#             a=np.array(a)
#             arraylist.append(a)
#         matrix=np.matrix(arraylist)
#         double_description.double_description(matrix, m, d)
# 
#         pass
#     
    def test_Cuboctahedron(self):
        file = open("cuboctahedron.poly", "r")
        #first_line = data.readline()
        first_line = file.readline()
        m,d = first_line.split()
        m=int(m)
        d=int(d)
        liste = file.readlines()
        arraylist=[]
        for line in liste:
            a=[int(i) for i in line.split()]
            a=np.array(a)
            arraylist.append(a)
        matrix=np.matrix(arraylist)
        print("Matrix Cubocta:   ", matrix)
        #print("Dimension Matrix Cubocta:  ", matrix.shape[0])
        W, m2 = double_description.double_description(matrix, m, d)
        print("Vertices nach DD:  ", m2)
        self.assertEqual(matrix, double_description.double_description(W, m2, d))
        pass
    
    
    def test_Cyclic(self):
        file = open("cyclic.poly", "r")
        #first_line = data.readline()
        first_line = file.readline()
        m,d = first_line.split()
        list = file.readlines()
        arraylist=[]
        for line in list:
            a=[int(i) for i in line.split()]
            a=np.array(a)
            arraylist.append(a)
        Matrix=np.matrix(arraylist)

        pass
    
    
    def test_Permutation(self):
        file = open("permutation.poly", "r")
        #first_line = data.readline()
        first_line = file.readline()
        m,d = first_line.split()
        list = file.readlines()
        arraylist=[]
        for line in list:
            a=[int(i) for i in line.split()]
            a=np.array(a)
            arraylist.append(a)
        Matrix=np.matrix(arraylist)

        pass
    
    
    def test_Simplex(self):
        file = open("simplex.poly", "r")
        #first_line = data.readline()
        first_line = file.readline()
        m,d = first_line.split()
        m=int(m)
        d=int(d)
        liste = file.readlines()
        arraylist=[]
        for line in liste:
            a=[int(i) for i in line.split()]
            a=np.array(a)
            arraylist.append(a)
        matrix=np.matrix(arraylist)
        #double_description.double_description(matrix, m, d)

        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()