#!/usr/bin/env python3
#import grass.script as gscript
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
import grass.script as gscript

class Test_v_random(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region',vector='boundary_state')


    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()


    def test_points(self):
        self.assertModule('v.random', output='test01', npoints=100, overwrite=True)


if __name__ == '__main__':
    test()