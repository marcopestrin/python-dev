from multiprocessing import Queue, Process, Value, Array, Lock
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()
        

if __name__ == "__main__":
    numbers = range(1,6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=square, args=(numbers, q))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())