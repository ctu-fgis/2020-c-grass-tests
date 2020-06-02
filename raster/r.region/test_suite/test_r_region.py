#!/usr/bin/env python3

from grass.gunittest.case import TestCase
from grass.gunittest.main import test

output = 'test03'
input = 'basins'
north = 228600
south = 215100
ref_extent="north=228600\nsouth=215100\neast=645000\nwest=630000"

class Test_r_region(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.use_temp_region()
        cls.runModule('g.region', raster = input)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

    def test_r_region(self):
        self.assertModule('g.copy', raster=(input, output), overwrite=True)
        self.assertModule('r.region', map=output, n=north, s=south)
        self.assertRasterFitsInfo(raster=output, reference=ref_extent)
if __name__ == '__main__':
    test()
