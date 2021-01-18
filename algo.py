from utile import *
import matplotlib.pyplot as plt

test = np.array([[0,0]])

def algo_naif(Y):
    S = []
    n=0

    for y in Y:
        dominated = False
        for y_ in Y[n:]:
            if dominate(y_,y):
                dominated=True
                break
        if not dominated:
            S.append(y)
        n+=1

    return np.array(S)

def algo_Q_4(T):
    # Tri
    T_tri = tri_sys(T)

    # Initialisation
    c2_min = T_tri[0, 1]
    T_nd = np.array([T_tri[0]])

    # Boucle
    for i in range(len(T_tri)):
        c2 = T_tri[i, 1]
        if c2_min > c2:
            T_nd = np.append(T_nd, [T_tri[i]], axis=0)
            c2_min = c2
    return T_nd

def algo_Q_7(k,Y):

    n = Y.shape[0]

    tab = []

    for i in range(k):
        tab.append([])
        for j in range(0,n-1):
            if i == 0:
                tab[i].append([[0,0]])
            elif i==j+1:
                tab[i].append([np.sum(Y[:j+1],axis=0)])
            elif j < i:
                tab[i].append([])
            else :
                tab[i].append(algo_Q_4(np.concatenate((tab[i][j-1],np.add(tab[i-1][j-1],Y[j+1])))))


    return np.array(tab[i][j])

def algo_Q_8(Y, I):
    min_max=np.inf
    min=0
    for y in Y:
        if y[0]>y[1]:
            alpha = I[1]
        else:
            alpha = I[0]
        r = (y[0]-y[1])*alpha + y[1]
        if r < min_max :
            min_max=r
            min=y
    return min

def algo_Q_9(k,T,I):

    return algo_Q_8(algo_Q_7(k,T),I)

def algo_transform(Y, I):
    Y2 = []
    for y in Y :
        y1_ = I[0]*y[0]+(1-I[0])*y[1]
        y2_ = I[1]*y[0]+(1-I[1])*y[1]
        Y2.append([y1_,y2_])
    return np.array(Y2)

def algo_reform_vector(Y, I):
    Y2 = []
    for y in Y :
        y1_ = ((1-I[0])*y[1]-(1-I[1])*y[0])/(I[1]-I[0]) #((1-amin)*y2'-(1-amax)*y1')/(amax-amin)
        y2_ = (I[0]*y[1]-I[1]*y[0])/(I[0]-I[1]) #(amin*y2'-amax*y1')/(amin-amax)
        Y2.append([y1_,y2_])
    return np.array(Y2)

def algo_reform(y,I):
    y1_ = ((1-I[0])*y[1]-(1-I[1])*y[0])/(I[1]-I[0]) #((1-amin)*y2'-(1-amax)*y1')/(amax-amin)
    y2_ = (I[0]*y[1]-I[1]*y[0])/(I[0]-I[1]) #(amin*y2'-amax*y1')/(amin-amax)
    return np.array([y1_,y2_])

def algo_Q_11(k,T,I):

    t = algo_transform(T,I)

    r = algo_Q_9(k,t,I)

    return algo_reform(r,I)
