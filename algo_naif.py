from utile import *

def algo_naif(Y):
    S = []
    n=0

    for y in Y:
        dominated = False
        for y' in Y[n:]:
            if dominate(y',y):
                dominated=True
                break
        if not dominated:
            S.append(y)
        n+=1

    return np.array(S)
