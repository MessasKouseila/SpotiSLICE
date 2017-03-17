import sys, traceback, Ice
import Demo
from threading import Thread
import time

class Streamer(Thread):
    

    def __init__(self, addip="127.0.0.1", port="5000"):
        Thread.__init__(self)
        self.ip = addip
        self.port = port
        self.adapteur = "Test"

    def run(self):
        arg = self.adapteur+":tcp -h "+self.ip+" -p "+self.port
        try:
            ic = Ice.initialize(sys.argv)
            base = ic.stringToProxy(arg)
            printer = Demo.PrinterPrx.checkedCast(base)
            if not printer:
                raise RuntimeError("Invalid proxy")
            while True:
                printer.printString("Hello World!")
                time.sleep(3)
        except:
            traceback.print_exc()
            status = 1

th = Streamer()
th.start()
for i in range(0, 10):
    print("je suis le thread principle")
    time.sleep(3)
th.join()
print("fin du game !!!!!!")