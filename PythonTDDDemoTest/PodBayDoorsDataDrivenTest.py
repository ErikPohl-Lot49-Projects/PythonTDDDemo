'''
Created on Jan 14, 2018

@author: Erik Pohl
'''

import parameterized as pm
import UnitedStatesSpacecraftDiscoveryOne.PodBayDoors as PBD
import unittest as ut

class PodBayDoorsDataDrivenTest(ut.TestCase):
    @pm.parameterized.expand([
 ##         TEST CASE NAME           TEST INPUT 1                            TEST INPUT 2          EXPECTED RESULT
        ("Open The Pod Bay Doors",   "Open The Pod Bay Doors",               "HAL",                "I'm sorry, Dave. I'm afraid I can't do that."),
        ("Is the Parrot Refundable", "Now that's what I call a dead parrot.","SHOP OWNER (Palin)", "No, no.....No,'e's stunned!"),
        ("What time is it?", "What time is it?",                             "MC Hammer",          "Stop, Hammer time!"),
    ])
    def testPodBayDoors(self, testname, testinp, testinp2, expected):
        self.assertEqual(PBD.PodBayDoorCommand(testinp, testinp2), expected)