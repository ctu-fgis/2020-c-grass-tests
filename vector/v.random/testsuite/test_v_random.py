#!/usr/bin/env python3
#import grass.script as gscript
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
import grass.script as gscript

output = 'test01'
npoints = 100
state = 'boundary_state'
zmin=10
zmax=120

class Test_v_random(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', vector=state)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

    def test_num_points(self):
        self.assertModule('v.random', output=output, npoints=npoints, overwrite=True)
        topology = dict(points=npoints)
        self.assertVectorFitsTopoInfo(vector=output, reference=topology)

    def test_num_points_3D(self):
        self.assertModule('v.random', output=output, npoints=npoints,
                          zmin=zmin, zmax=zmax,
                          overwrite=True, flags='z')

        topology = dict(points=npoints, map3d=1)
        self.assertVectorFitsTopoInfo(vector=output, reference=topology)
        
if __name__ == '__main__':
    test()
