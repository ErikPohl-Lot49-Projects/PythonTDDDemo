'''
Created on Jan 7, 2018

@author: Erik Pohl
'''
import parameterized as pm
import PythonTDDDemo.RedGreenRefactor as RGR
import unittest as ut

class RedGreenRefactorDataDrivenTest(ut.TestCase):
##load test cases from a database using sqllite3
    @pm.parameterized.expand([
        ("Red and Even to Green", 2,RGR.RED, RGR.GREEN),
        ("Red and Odd to Red", 3,RGR.RED, RGR.RED),
        ("Red and Even to Green", 4,RGR.RED, RGR.GREEN),
        ("Red and Odd to Red", 5,RGR.RED, RGR.RED),
        ("Red and Even to Green", 10,RGR.RED, RGR.GREEN),
        ("Green and Odd to Refactor", 3,RGR.GREEN, RGR.REFACTOR),
        ("Green and Even to Green", 4,RGR.GREEN, RGR.GREEN),
        ("Green and Odd to Refactor", 7,RGR.GREEN, RGR.REFACTOR),
        ("Refactor and Divisible by 10 to Red", 10,RGR.REFACTOR, RGR.RED),
        ("Refactor and Divisible by 10 to Red", 30,RGR.REFACTOR, RGR.RED),
        ("Refactor and Divisible by 10 to Red", 10,RGR.REFACTOR, RGR.RED),
        ("Refactor and Divisible by 10 to Red", 30,RGR.REFACTOR, RGR.RED),
        ("Refactor and not Divisible by 10 to Refactor", 31,RGR.REFACTOR, RGR.REFACTOR),
        ("Green and Even to Green", 8,RGR.GREEN, RGR.GREEN),
    ])
    def testRedGreenRefactor(self, testname, testinp, testinp2, expected):
        self.assertEqual(RGR.ChangeState(testinp, testinp2), expected)