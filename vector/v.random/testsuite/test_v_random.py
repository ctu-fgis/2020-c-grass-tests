#!/usr/bin/env python3

import grass.script as gscript

# v.random output=test01 npoints=100
gscript.run_command('v.random', output='test01', npoints=100, overwrite=True)

# 1. Rewrite into testsuite
# 2. Check output vector map - number of points