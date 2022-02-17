import sys
from copy import deepcopy

n_clause = 91
n_lit = 20


model_dict={}

list=[]

for i in range(1,n_lit+1):
    model_dict[i]=0
    list.append(i)


def sat_solver(cnf):
    temp_true=[]
    temp_false=[]
    clauses=[]

    for clause in cnf:
        if len(clause) == 1:
            clauses.append(clause)
            cnf.remove(clause)

    for clause in clauses :
        if(clause < 0):
            model_dict[clause] = -1
            temp_false.append(clause)
        else:
            model_dict[clause] = 1
            temp_true.append(clause)
    
    for clause in cnf:
        for l in clause:
            if model_dict[abs(l)] == 1:
                cnf.remove(clause)
                list.remove(abs(l))
                break
            elif model_dict[abs(l)] == -1:
                clause.remove(l)
                list.remove(abs(l))
                if(len(clause) == 0):
                    return 0
                break

    if len(cnf) == 0:
        return 1

    for x in list:
        cnf1 = deepcopy(cnf) + [x]
        cnf2 = deepcopy(cnf) + [-x]
        if(sat_solver(sat_solver(cnf1))):
            return 1
        if(sat_solver(sat_solver(cnf2))):
            return 1
    return 0


def dpll(cnf):
    #Take inputs 
    #Convert it to literals
    #solve cnf
    cnf = [ [1], [2], [1,2]]
    print(sat_solver(cnf))
    return
