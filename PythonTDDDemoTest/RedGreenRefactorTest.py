'''
TDDDemo/PythonTDDDemoTest/RedGreenRefactorTest.py
Created on Jan 7, 2018

@author: Erik Pohl
'''

import PythonTDDDemo.RedGreenRefactor as RGR
import unittest as ut

##State            
##Red                          if file length is even, change the state to Green
##Green                        if file length is odd, change the state to refactor
##Refactor                     if # of chars in file is divisible by 10, change the state to Red

class RedGreenRefactorTest(ut.TestCase):
    def testRedToGreen(self):
        self.assertEqual(RGR.ChangeState(2,'Red'), RGR.GREEN, 'Expected '+ RGR.GREEN)   ## red and even moves to green
        self.assertEqual(RGR.ChangeState(3,RGR.RED), RGR.RED, 'Expected '+ RGR.RED)     ## red and odd stays red
        self.assertEqual(RGR.ChangeState(4,RGR.RED), RGR.GREEN, 'Expected '+ RGR.GREEN) ## red and even moves to green
        self.assertEqual(RGR.ChangeState(5,RGR.RED), RGR.RED, 'Expected '+ RGR.RED)     ## red and odd stays red
        self.assertEqual(RGR.ChangeState(10,RGR.RED), RGR.GREEN, 'Expected '+ RGR.GREEN) ## red and even moves to green
    def testGreentoRefactor(self):
        self.assertEqual(RGR.ChangeState(3,RGR.GREEN), RGR.REFACTOR, 'Expected ' + RGR.REFACTOR) ## green and odd moves to refactor
        self.assertEqual(RGR.ChangeState(4,RGR.GREEN), RGR.GREEN, 'Expected ' + RGR.GREEN)       ## green and even stays green
        self.assertEqual(RGR.ChangeState(7,RGR.GREEN), RGR.REFACTOR, 'Expected ' + RGR.REFACTOR) ## green and odd moves to refactor
    def testRefactortoRed(self):
        self.assertEqual(RGR.ChangeState(10,RGR.REFACTOR), RGR.RED, 'Expected ' + RGR.RED)
        self.assertEqual(RGR.ChangeState(30,RGR.REFACTOR), RGR.RED, 'Expected ' + RGR.RED)
        
        



