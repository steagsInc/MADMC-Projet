import os,time
from utile import *
from algo import *
import matplotlib.pyplot as plt

def Q5():

    m=1000
    max = 10001

    time_Q3 = []
    time_Q4 = []

    for n in range(200,max,200):

        mean_Q3 = 0
        mean_Q4 = 0

        print("n :",n)

        for i in range(50):
            t=time.time()
            algo_naif(generate_Y(n,m))
            t=time.time()-t
            mean_Q3+=t

            t=time.time()
            algo_Q_4(generate_Y(n,m))
            t=time.time()-t
            mean_Q4+=t

        time_Q3.append(mean_Q3/50)
        time_Q4.append(mean_Q4/50)

    n = np.array(range(200,max,200))

    plt.plot(n, np.array(time_Q3),'c',label='naif')
    plt.plot(n, np.array(time_Q4),'r',label='amélioré')
    plt.ylabel('Time')
    plt.xlabel('n')
    plt.legend()
    plt.show()

def Q12():

    n=50
    k=10
    m=1000

    time_Q3 = []
    time_Q4 = []

    for e in range(25,501,25):

        I = [0.5-e/1000,0.5+e/1000]

        mean_Q3 = 0
        mean_Q4 = 0

        print("e :",e/1000)

        for i in range(50):
            Y = generate_Y(n,m)

            t=time.time()
            algo_Q_9(10,Y,I)
            t=time.time()-t
            mean_Q3+=t

            t=time.time()
            algo_Q_11(10,Y,I)
            t=time.time()-t
            mean_Q4+=t

        time_Q3.append(mean_Q3/50)
        time_Q4.append(mean_Q4/50)

    n = np.array(range(25,501,25))
    n = n/1000

    plt.plot(n, np.array(time_Q3),'c',label='Partie 3')
    plt.plot(n, np.array(time_Q4),'r',label='Partie 4')
    plt.ylabel('Time')
    plt.xlabel('ε')
    plt.legend()
    plt.show()

def plot_transformed(Y,I):

    Y = generate_Y(50,50)

    t = algo_transform(Y,I)

    x = np.array(range(80))

    plt.scatter(Y[:,0],Y[:,1],label='Y')
    plt.scatter(t[:,0],t[:,1],label='t')
    plt.plot(x,x,'c')
    plt.legend()
    plt.show()

def front(k,Y,I):

    t = algo_transform(Y,I)

    P3 = algo_Q_7(k,Y)

    P4 = algo_reform_vector(algo_Q_7(k,t),I)

    print(P3.shape)
    print(P4.shape)

    plt.scatter(P3[:,0],P3[:,1],label='Partie 3')
    plt.scatter(P4[:,0],P4[:,1],label='Partie 4')
    plt.legend()
    plt.show()

I = [0.5-0.025,0.5+0.025]

Y = generate_Y(50,100)

#plot_transformed(Y,I)

Q5()
Q12()
