#!/usr/bin/env python3

from grass.gunittest.case import TestCase
from grass.gunittest.main import test
import grass.script as gscript

output = 'test1'
stats = 'lakes'
data = [['34300=44200.000000'],
        ['39000=3509900.000000'],
        ['43600=47000.000000']]


class Test_r_stats(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', raster = stats)


    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

# testing total area 
    def test_check_area(self):
        #self.assertModule('r.stats', input = stats , flags = 'aN')
        module = self.assertModule('r.stats', input = stats , flags = 'aN',separator = '=')
        print(self.assertModule('r.stats', input = stats , flags = 'aN',separator = '='))
       #self.assertModuleKeyValue(module,
        #                          reference=dict('34300'='44200' , '39000'='3509900' , '43600'='47000'),
        #                          precision=1, sep='=')
        self.assertEqual(data,module)
if __name__ == '__main__':
    test()