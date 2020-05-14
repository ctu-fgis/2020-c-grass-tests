#!/usr/bin/env python3
#import grass.script as gscript
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
import grass.script as gscript


output='test01'

npoints=100

state='boundary_state'



zmin=10



zmax=120


class Test_v_random(TestCase):


    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region',vector=state)


    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()


    def test_points(self):
        self.assertModule('v.random', output=output, npoints=npoints, overwrite=True)
        topology = dict(points=npoints)
        self.assertVectorFitsTopoInfo(vector=output, reference=topology)


    def test_points3D(self):
        self.assertModule('v.random',output=output,npoints=npoints, zmin=zmin,zmax=zmax,column='height',overwrite=True,flags='z')
        

        topology = dict(points=npoints)

        self.assertVectorFitsTopoInfo(vector=output, reference=topology)



        self.assertModuleKeyValue('v.info', map=output, flags='etg',
                                  sep="=", precision=5, layer="1",
                                  reference=dict(name=output,
                                                 num_dblinks=1,
                                                 attribute_layer_name=output,
                                                 attribute_layer_number=1,
                                                 attribute_database_driver="sqlite",
                                                 attribute_table=output,
                                                 bottom=zmin,
                                                 top=zmax))
                                                 #where="bottom>zmin and top<zmax"))
        #self.assertModule('v.info',map=output, flags='etg')
        #self.assertVectorFitsUnivar(map=output, column='height', reference=topology, msg=None, layer=output, type=None, where="bottom>zmin and top<zmax", precision=0.1)
        #self.assertRasterMinMax(map=output, refmin=zmin, refmax=zmax)


        #self.assertModuleKeyValue('v.info', map=state, flags='gr',

                          #reference=dict(min=zmin, max=zmax),

                          #precision=0.01, sep='=')

    def test_points_restrict (self):

        self.assertModule('v.random',output=output,npoints=npoints,restrict=state,overwrite=True)

        topology=dict(points=npoints)
        self.assertVectorFitsTopoInfo(vector=output, reference=topology)
        #self.assertVectorFitsTopoInfo(vector=state, reference=topology)
        #self.assertVectorFitsRegionInfo(vector=state, precision=0.1,reference=topology)


if __name__ == '__main__':
    test()