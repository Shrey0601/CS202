from pysat.solvers import Glucose3, Solver
import pandas as pd
import numpy as np
import random
import time

k=int(input("Enter the value of k: "))
n=k*k

start_time = time.time()


def variable(row, column, digit, matrix):
  return int((matrix-1)*n*n*n+(row-1)*n*n+(column-1)*n+digit)

def devariable(var):
    var=int(var)
    var = var - 1
    matrix = int(var/(n*n*n))
    var%=(n*n*n)
    row = int(var/(n*n))
    var %= (n*n)
    col =int(var/n)
    var %= n
    digit = int(var) 

    return (matrix+1, row+1, col+1, digit+1)

def devariable2(var):
    var=int(var)
    var = var - 1
    row = int(var/n)
    col = var%n
    return (row+1, col+1)

def Sudoku(df, bclause, cl):
 clause = []
 for row in range(1,n+1):
  for column in range(1,n+1):
    if df[row-1][column-1]!=0 :                                
      clause.append([variable(row, column, df[row-1][column-1], 1)])

 for row in range(n+1,2*n+1):
  for column in range(1,n+1):
    if df[row-1][column-1]!=0 :
      clause.append([variable(row-n, column, df[row-1][column-1], 2)])

 
 ans = 0
 s = Solver()
 for c in clause:
  s.add_clause(c)
 s.add_clause(cl)
 for c in bclause:
  s.add_clause(c)
 if(s.solve()):
   return 0
 else:
   return 1


df = np.zeros([2*n,n], dtype=int)

bclause = []

for row in range(1, n+1):
  for column in range(1,n+1):
    bclause.append([variable(row,column, digit,1) for digit in range(1,n+1)])
    bclause.append([variable(row,column, digit,2) for digit in range(1,n+1)])
    for digit in range(1,n+1):
      for num in range(digit+1, n+1):
        bclause.append([-variable(row, column, digit, 1), -variable(row, column, num, 1)])
        bclause.append([-variable(row, column, digit, 2), -variable(row, column, num, 2)])

for digit in range(1,n+1):
  for row in range(1,n+1):
    bclause.append([variable(row, column, digit, 1) for column in range(1,n+1)])
    bclause.append([variable(row, column, digit, 2) for column in range(1,n+1)])
    for column in range(1, n+1):
      for column1 in range(column+1, n+1):
        bclause.append([-variable(row, column, digit, 1), -variable(row, column1, digit, 1)])
        bclause.append([-variable(row, column, digit, 2), -variable(row, column1, digit, 2)])

  for column in range(1,n+1):
    bclause.append([variable(row, column, digit, 1) for row in range(1,n+1)]) 
    bclause.append([variable(row, column, digit, 2) for row in range(1,n+1)]) 
    for row in range(1, n+1):
      for row1 in range(row+1, n+1):
        bclause.append([-variable(row, column, digit, 1), -variable(row1, column, digit, 1)])
        bclause.append([-variable(row, column, digit, 2), -variable(row1, column, digit, 2)])

  for subrow in range(0,k):
    for subcolumn in range(0,k):
      bclause.append([int(variable(subrow*k+rowdig, subcolumn*k+coldig, digit, 1)) for rowdig in range(1,k+1) for coldig in range(1,k+1)])
      bclause.append([int(variable(subrow*k+rowdig, subcolumn*k+coldig, digit, 2)) for rowdig in range(1,k+1) for coldig in range(1,k+1)])
      for ind in range(1,k+1):
        for ind1 in range(1,k+1):
          for ind2 in range(ind+1,k+1):
            for ind3 in range(ind1+1,k+1):
              bclause.append([-variable(subrow*k+ind,subcolumn*k+ind1,digit, 1),-variable(subrow*k+ind2,subcolumn*k+ind3,digit, 1)])
              bclause.append([-variable(subrow*k+ind,subcolumn*k+ind1,digit, 2),-variable(subrow*k+ind2,subcolumn*k+ind3,digit, 2)])


for row in range(1,n+1):
  for column in range(1,n+1):
    for digit in range(1,n+1):
      bclause.append([-variable(row, column, digit, 1), -variable(row, column, digit, 2)])


s = Solver()
for c in bclause:
  s.add_clause(c)
  #print(c)

cl = []
if(s.solve()):
  model = s.get_model()
  for x in model:
    cl.append(-x) 
    if x>0:
      (matrix, row, col, digit) = devariable(int(x))
      df[row-1+(matrix-1)*n][col-1] = digit

list = []
for i in range(1,(n**2)*2 + 1):
    list.append(i)

random.shuffle(list)


for i in list:
    (r,c) = devariable2(i)
    x = df[r-1][c-1]
    df[r-1][c-1] = 0
    if(Sudoku(df, bclause, cl)):
        continue
    else:
        df[r-1][c-1] = x

print("--- %s seconds ---" % (time.time() - start_time))

df = pd.DataFrame(df)
print(df)

df.to_csv("output_sudoku_pair.csv", header=False, index=False)    

