import time #pip install time
import math
from threading import Thread

def numPar(n):
    time_ini = time.time()
    for i in range(n):
        if i % 2 == 0:
            print(i)

    print("Total: ", math.floor(n/2))
    time_end = time.time()
    total = time_end - time_ini
    print("Tiempo: ",total)

numPar(10)
t = Thread(target=numPar, args=("n"))
t.start()