import os,time
from utile import *
from algo_naif import *
import matplotlib.pyplot as plt

m=1000
max = 10001

def mesure():

    time_Q3 = []
    time_Q4 = []

    for n in range(200,max,200):

        mean_Q3 = 0
        mean_Q4 = 0

        print("n :",n)

        for i in range(50):
            t=time.time()
            algo_naif(generate_X(n,m))
            t=time.time()-t
            mean_Q3+=t

            t=time.time()
            algo_Q_4(generate_X(n,m))
            t=time.time()-t
            mean_Q4+=t

        time_Q3.append(mean_Q3/50)
        time_Q4.append(mean_Q4/50)

    n = np.array(range(200,max,200))

    plt.plot(n, np.array(time_Q3),'c',label='Q3')
    plt.plot(n, np.array(time_Q4),'r',label='Q4')
    plt.legend()
    plt.show()


mesure()
