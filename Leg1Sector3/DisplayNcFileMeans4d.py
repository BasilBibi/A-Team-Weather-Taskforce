import netCDF4 as nc
import numpy as np
import sys

ds=nc.Dataset('./data.nc')

results=[ds[sys.argv[1]][i:i+4].mean(0)[0][0][0] for i in range(0,40,4)]
print( ','.join(map(str,results)))
