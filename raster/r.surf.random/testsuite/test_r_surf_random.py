#!/usr/bin/env python3

from grass.gunittest.case import TestCase
from grass.gunittest.main import test

output = 'test01'
n=100
s=-100
w=-100
e=100
res=1
min=10
max=40

class Test_v_surf_random(TestCase):

# setting up computational region
    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', n=n, s=s, e=e, w=w, res=res)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

# testing if output parameters are between input parameters
    def test_min_max(self):
         self.assertModule('r.surf.random', output=output, min=min, max=max, overwrite=True)
         self.assertRasterMinMax(map=output, refmin=min, refmax=max)

if __name__ == '__main__':
    test()
