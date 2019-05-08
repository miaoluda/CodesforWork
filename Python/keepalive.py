#!/usr/bin/env python 
# -*- coding: UTF-8 -*-

import sys
import time
# Compatible with python2: thread and pytho3: _thread 
try:
    import thread 
except ModuleNotFoundError:
    import _thread

# Compatible with python2 and python3 
try:
    thread = _thread
    raw_input = input
except NameError:
    pass



starttime = time.time()

def getPassedtime():
    n =  time.time() - starttime
    if n < 60:
        return  '{0:.4f} s'.format(n)
    else:
        m = int(n // 60)
        nn = n - m*60.0
        return '{0:d} min {1:.4f} s'.format(m, nn)

# keyboard input
def input_thread(L):
    raw_input()
    L.append(None)
L = []
thread.start_new_thread(input_thread, (L,))

print("Trying to keep this ssh session alive...")

print("Press Enter to break")

while True:
    if L: break
    time.sleep(0.1)
    if L: 
        print('')
        break
    n =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    passedtime = '{0:.4f}'.format(time.time() - starttime)
    # use sys.stdout to stop from printing in new lines.
    sys.stdout.write('\rCurrent time: {0}, {1} has gone...\r'.format(n,getPassedtime()))
    sys.stdout.flush()
