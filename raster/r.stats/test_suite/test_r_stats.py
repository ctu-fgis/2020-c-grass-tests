#!/usr/bin/env python3

from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.gunittest.gmodules import call_module

input = 'lakes'
#count of pixels with different ID
ref_stats = '34300 442\n39000 35099\n43600 470\n* 1988989'
#area of pixels with different ID
ref_stats2 = '34300 44200.000000\n39000 3509900.000000\n43600 47000.000000'

class Test_r_stats(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', raster = input)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

    # Testing total area 
    def test_number_of_pixels(self):
        stats = call_module('r.stats', input=input, flags='c').rstrip('\n')
        self.assertEqual(stats, ref_stats)

    def test_area(self)
        stats = call_module('r.stats', input=input, flags='aN').rstrip('\n')
        self.assertEqual(stats, ref_stats2)


if __name__ == '__main__':
    test()