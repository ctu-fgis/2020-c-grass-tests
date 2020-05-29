#!/usr/bin/env python3
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
import grass.script as gscript

output = 'test05'
buffer = 'basins'
distance1=100
distance2=200

class Test_r_buffer(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
#        cls.runModule('g.region', raster=buffer)


    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

#create buffer with distance 100 metres
    def test_check_distance(self):
        self.assertModule('r.buffer', output=output, input=buffer, overwrite=True, distances=distance1)
        self.assertRastersDifference(actual='buffer', reference='output', precision=0.5, statistics=None)
#otestovat, jestli se souøadnice nejjižnejších a nejsevernìjších posunuly o 100

if __name__ == '__main__':
    test()