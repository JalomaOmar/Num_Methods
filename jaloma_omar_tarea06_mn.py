# -*- coding: utf-8 -*-
"""Jaloma_Omar_Tarea06_MN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iPbbtbqDi3RckwN2sQfeS1HqcIxBhuUn
"""

import numpy as np
#INCISO B
def CholeskyTridiagonal(D):
    n=D.shape[0]
    E=np.empty([n,n])
    E.fill(0)
    for k in range(n):
      if k==0:
        E[0,0]=np.sqrt(D[0,0])
      else:
        A=np.empty([k,k])
        A.fill(0)
        for i in range(k):
          for j in range(k-i):
            A[i][j]=E[j][k-1-i-j]
        b=np.empty(k)
        b.fill(0)
        b[0]=D[k-1][1]
        x=np.linalg.solve(A,b)
        for l in range(k):
          E[l][k-l]=x[l]
        E[k][0]=np.sqrt(D[k][0]-np.sum(x**2))
    return(E)

#PRUEBA

D=np.array([4,1,5,1,6,0]) #Este ejemplo lo hice a mano y sí funcionó
D=D.reshape([3,2])

print(CholeskyTridiagonal(D))
print('\n----------------------------------------\n')

#INCISO C

def DetCholeskyTridiagonal(D):
  A=CholeskyTridiagonal(D)
  n=A.shape[0]
  r=1
  for i in range(n):
    r*=(A[i][0]**2) #Esto se debe a que el determinante es multiplicativo y el determinante de una matriz triangular es el producto de la diagonal
  return(r)

print(DetCholeskyTridiagonal(D)) #Coincide con el resultado a mano
print('\n----------------------------------------\n')

def SolverCholeskyTridiagonal(D, b):
  E=CholeskyTridiagonal(D)
  n=E.shape[0]
  U=[]
  for i in range(n):
    if i==0:
      U=U+list(E[i])
    else:
      U=U+list(E[i])[n-i:]+list(E[i])[:n-i]
  U=np.array(U)
  U=U.reshape([n,n]) #Hasta aquí obtenemos a U a partir de E
  y=np.linalg.solve(U.transpose(), b) #Forward
  x=np.linalg.solve(U,y) #Backward
  return(x)

b=np.array([5,7,7])
print(SolverCholeskyTridiagonal(D,b))
print('--------------------------------')