#!/usr/bin/env python3


from grass.gunittest.case import TestCase
from grass.gunittest.main import test
import grass.script as gscript

output = 'test01'
input = 'basins'
resolution = 20
north = 228500
south = 215000
east = 645000
west = 630000
min=2
max=30


class Test_r_resample(TestCase):

    @classmethod

    def setUpClass(cls):

        cls.use_temp_region()
#change of resolution from 10 to 20 
        cls.runModule('g.region', raster = input, res = resolution)

    @classmethod

    def tearDownClass(cls):

        cls.del_temp_region()

    def test_check_resample(self):
#running funciton r.resample
        self.assertModule('r.resample', input = input, output = output, overwrite = True)
#testing resolution
        self.assertModuleKeyValue('r.info', map = output, flags = 'gr',
                          reference = dict(nsres = resolution , ewres = resolution),
                          precision = 0.01, sep = '=')
#testing coordinates
        self.assertModuleKeyValue('r.info', map = output, flags = 'gr',
                          reference = dict(north = north, west = west, east = east, south = south),
                          precision = 0.01, sep = '=')
#testing data values
        self.assertModuleKeyValue('r.info', map = output, flags = 'gr',
                          reference = dict(min=min , max=max),
                          precision = 0.01, sep = '=')

if __name__ == '__main__':

    test()