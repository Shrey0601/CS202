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
    if len(cnf) == 0:
        return 1
    temp_true=[]
    temp_false=[]
    clauses=[]

    for clause in cnf:
        if len(clause) == 1:
            clauses.append(clause[0])
            cnf.remove(clause)

    for clause in clauses :
        if(clause < 0):
            model_dict[abs(clause)] = -1
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
    return sat_solver(cnf)

    # for x in list:
    #     cnf1 = deepcopy(cnf) + [x]
    #     cnf2 = deepcopy(cnf) + [-x]
    #     if(sat_solver(cnf1)):
    #         return 1
    #     if(sat_solver(cnf2)):
    #         return 1
    # return 0



# cnf = []
# with open("uf20-011.cnf") as f:
#     for line in f:
#         if not (line.startswith("c") or line.startswith("p")):
#             cnf.append([int(x) for x in line.rstrip("0").rstrip("0\n").split()])
cnf = [[1,2], [2,3]]
print(sat_solver(cnf))
