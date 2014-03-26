#!/bin/python
from threading import Timer 
import serial
delayTime = 0.5
currentCount = 0
portAddr = '/dev/ttyS0'
port = serial.Serial(portAddr);
port.timeout = 1
exitFlag=False

def onTimerEnd():
  global currentCount
  print currentCount
  currentCount=0

def readDataFromPort():
  global currentCount
  messageTimer = Timer(delayTime, onTimerEnd)
  while True:
    result = port.read()
    if len(result)!=0:
      currentCount += 1
      messageTimer.cancel()
      messageTimer = Timer(delayTime, onTimerEnd)
      messageTimer.start()
readDataFromPort()


