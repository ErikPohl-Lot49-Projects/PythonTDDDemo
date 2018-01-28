'''
TDDDemo/PythonTDDDemo/RGRToolSet.py
Created on Jan 7, 2018

@author: Erik Pohl
'''
import os

def RGRFileLength(FileName):
    return os.path.getsize(FileName)
 
def RGRAddComment(FileName, Comment):
    file = open(FileName,"a")
    file.write(Comment)
    file.close()



    
    
    