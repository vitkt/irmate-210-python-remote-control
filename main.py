#!/bin/python
from threading import Timer 
from threading import Thread
import sys
import serial
delayTime = 0.5
currentCount = 0
portAddr = '/dev/ttyS0'
port = serial.Serial(portAddr);
port.timeout = 1
exitFlag=False

def handler(result):
  print result

def onTimerEnd():
  global currentCount
  handlerThread = Thread(target=handler, args = (currentCount,))
  handlerThread.start()
  currentCount=0

def readDataFromPort():
  global currentCount
  messageTimer = Timer(delayTime, onTimerEnd)
  while True:
    sys.stdout.flush()
    result = port.read()
    if len(result)!=0:
      currentCount += 1
      messageTimer.cancel()
      messageTimer = Timer(delayTime, onTimerEnd)
      messageTimer.start()
readDataFromPort()


