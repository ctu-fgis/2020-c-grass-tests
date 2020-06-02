#!/usr/bin/env python3

from grass.gunittest.case import TestCase
from grass.gunittest.main import test

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

        # change of resolution from 10 to 20 
        cls.runModule('g.region', raster=input, res=resolution)

    @classmethod
    def tearDownClass(cls):
        cls.del_temp_region()

    def test_check_resample(self):
        # running r.resample
        self.assertModule('r.resample', input=input, output=output, overwrite=True)

        # testing resolution
        ref_res="nsres=20\newres=20"
        self.assertRasterFitsInfo(raster=output, reference=ref_res)

        # testing coordinates
        ref_extent="north=228500\nsouth=215000\neast=645000\nwest=630000"
        self.assertRasterFitsInfo(raster=output, reference=ref_extent)
        
        # testing data values
        ref_values="min=2\nmax=30"
        self.assertRasterFitsInfo(raster=output, reference=ref_values)

if __name__ == '__main__':
    test()
