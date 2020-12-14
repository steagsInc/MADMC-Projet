from utile import *

test = np.array([[0,0]])

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

print(algo_Q_7(5,generate_Y(10,10)))

def algo_Q_8(y, I):
    if y[0]>y[1]:
        alpha = I[1]
    else:
        alpha = I[0]
    return (y[0]-y[1])*alpha + y[1]

def algo_Q_9(T):

    return (y[0]-y[1])*alpha + y[1]
