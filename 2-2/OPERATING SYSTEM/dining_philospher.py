import threading
import random
import time

#inheriting threading class in Thread module
class Philosopher(threading.Thread):
    running = True  
    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            time.sleep(3)
            print ('Philosopher %s is hungry.' % self.index)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire() 
            locked = fork2.acquire(False) 
            if locked: break 
            fork1.release()
            print ('Philosopher %s swaps forks.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()
 
    def dining(self):           
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(2)
        print ('Philosopher %s finishes eating and leaves to think.' % self.index)

def main():
    forks = [threading.Semaphore() for n in range(5)] #initialising array of semaphore i.e forks

    #here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers= [Philosopher(i, forks[i%5], forks[(i+1)%5])
            for i in range(5)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(5)
    Philosopher.running = False
    print ("Now we're finishing.")
 

if __name__ == "__main__":
    main()
    
    
'''
Philosopher 1 is hungry.
Philosopher 1 starts eating. 
Philosopher 0 is hungry.Philosopher 3 is hungry.
Philosopher 3 starts eating. Philosopher 2 is hungry.
Philosopher 4 is hungry.Philosopher 0 swaps forks.
Philosopher 1 finishes eating and leaves to think.
Now we're finishing.
Philosopher 2 swaps forks.
Philosopher 0 starts eating.
Philosopher 3 finishes eating and leaves to think.
Philosopher 4 swaps forks.
Philosopher 0 finishes eating and leaves to think.
Philosopher 1 is hungry.


'''