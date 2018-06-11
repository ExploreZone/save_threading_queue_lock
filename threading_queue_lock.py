#coding:utf-8

import Queue
import threading
import time

ExitFlag =0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "starting: " + self.name
        process_data(self.name,self.q)
        print "Exiting" + self.name
        print
def process_data(threadName,q):
    while not ExitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            print "%s processing %s"%(threadName,data)
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(1)



threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["one","two","three","four","five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads =[]
threadID = 1

for tName in nameList:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass
ExitFlag = 1

for t in threads:
    t.join()
print "exiting main thread"