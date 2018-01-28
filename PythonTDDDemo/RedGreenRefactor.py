'''
TDDDemo/PythonTDDDemo/RedGreenRefactor.py
Created on Jan 7, 2018

@author: Erik Pohl
'''

import PythonTDDDemo.RGRToolSet as RGRT
from _weakref import ref


##State            
##Red                          if file length is even, change the state to Green
##Green                        if file length is odd, change the state to refactor
##Refactor                     if # of chars in file is divisible by 10, change the state to Red

GREEN = "Green"
REFACTOR = "Refactor"
RED = "Red"

def ChangeState(FileLength, CurrentState):    
    if (CurrentState == REFACTOR) and (FileLength % 10 == 0):
        return RED
    if (CurrentState == GREEN) and (FileLength % 2 == 1):
        return REFACTOR
    if (CurrentState == RED) and (FileLength % 2 == 0):
        return GREEN
    return CurrentState

def Main():
    CurrentState = RED
    ThisVeryFile = 'C:\\Users\\Richard Pendrake\\eclipse-workspace\\TDDDemo\\PythonTDDDemo\\RedGreenRefactor.py'
    for iterate in range(1,20):
        RGRT.RGRAddComment(ThisVeryFile, "#")
        FileLength = RGRT.RGRFileLength(ThisVeryFile)
        CurrentState = ChangeState(FileLength,CurrentState)
        print(FileLength)
        print(CurrentState)
    
Main()#############################################################################