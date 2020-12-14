from utile import *

def algo_naif(X):
    S = []

    for x in X:
        dominated = False
        for y in X:
            if dominate(y,x):
                dominated=True
                break
        if not dominated:
            S.append(x)

    return np.array(S)
