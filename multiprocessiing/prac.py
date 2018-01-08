from multiprocessing import Process, Queue, Pool
from time import sleep

def abc(a):

    for i in range(100000):
        print(a, str(i))


if __name__ == '__main__':

    p = Pool(5)
    for i in range(10):
        Process(target=abc,args=(i,)).start()

