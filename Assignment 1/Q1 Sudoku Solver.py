from pysat.solvers import Glucose3, Solver
import pandas as pd
import time
import math

start = time.time()
df=pd.read_csv('tests\test_3_T.csv', header=None).values  
#Add path of the testfile in FileName
(a,b) = df.shape
k = int(math.sqrt(b))
n = b


def variable(row, column, digit, matrix):
  return (matrix-1)*n*n*n+(row-1)*n*n+(column-1)*n+digit

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

clause = []
for row in range(1, n+1):
  for column in range(1,n+1):
    clause.append([int(variable(row,column, digit,1)) for digit in range(1,n+1)])
    clause.append([int(variable(row,column, digit,2)) for digit in range(1,n+1)])
    for digit in range(1,n+1):
      for num in range(digit+1, n+1):
        clause.append([int(-variable(row, column, digit, 1)), int(-variable(row, column, num, 1))])
        clause.append([int(-variable(row, column, digit, 2)), int(-variable(row, column, num, 2))])

for digit in range(1,n+1):
  for row in range(1,n+1):
    clause.append([int(variable(row, column, digit, 1)) for column in range(1,n+1)])
    clause.append([int(variable(row, column, digit, 2)) for column in range(1,n+1)])
    for column in range(1, n+1):
      for column1 in range(column+1, n+1):
        clause.append([int(-variable(row, column, digit, 1)), int(-variable(row, column1, digit, 1))])
        clause.append([int(-variable(row, column, digit, 2)), int(-variable(row, column1, digit, 2))])

  for column in range(1,n+1):
    clause.append([int(variable(row, column, digit, 1)) for row in range(1,n+1)]) 
    clause.append([int(variable(row, column, digit, 2)) for row in range(1,n+1)]) 
    for row in range(1, n+1):
      for row1 in range(row+1, n+1):
        clause.append([int(-variable(row, column, digit, 1)), int(-variable(row1, column, digit, 1))])
        clause.append([int(-variable(row, column, digit, 2)), int(-variable(row1, column, digit, 2))])

  for subrow in range(0,k):
    for subcolumn in range(0,k):
      clause.append([int(variable(subrow*k+rowdig, subcolumn*k+coldig, digit, 1)) for rowdig in range(1,k+1) for coldig in range(1,k+1)])
      clause.append([int(variable(subrow*k+rowdig, subcolumn*k+coldig, digit, 2)) for rowdig in range(1,k+1) for coldig in range(1,k+1)])
      for ind in range(1,k+1):
        for ind1 in range(1,k+1):
          for ind2 in range(ind+1,k+1):
            for ind3 in range(ind1+1,k+1):
              clause.append([-1*variable(subrow*k+ind,subcolumn*k+ind1,digit, 1),-1*variable(subrow*k+ind2,subcolumn*k+ind3,digit, 1)])
              clause.append([-1*variable(subrow*k+ind,subcolumn*k+ind1,digit, 2),-1*variable(subrow*k+ind2,subcolumn*k+ind3,digit, 2)])


for row in range(1,n+1):
  for column in range(1,n+1):
    if df[row-1][column-1]!=0 :                                
      clause.append([int(variable(row, column, df[row-1][column-1], 1))])

for row in range(1,2*n+1):
  for column in range(1,n+1):
    if df[row-1][column-1]!=0 :
      clause.append([int(variable(row-n, column, df[row-1][column-1], 2))])

for row in range(1,n+1):
  for column in range(1,n+1):
    for digit in range(1,n+1):
      clause.append([int(-variable(row, column, digit, 1)), int(-variable(row, column, digit, 2))])

s = Solver()
for c in clause:
  s.add_clause(c)

if(s.solve()):
  model = s.get_model()
  for x in model:
    if x>0:
      (matrix, row, col, digit) = devariable(int(x))
      df[row-1+(matrix-1)*n][col-1] = digit

  df = pd.DataFrame(df)
  print(df)

  df.to_csv("output_sudoku_pair.csv", header=False, index=False)

else:
  print("No pair possible")


end = time.time()
print(end - start)