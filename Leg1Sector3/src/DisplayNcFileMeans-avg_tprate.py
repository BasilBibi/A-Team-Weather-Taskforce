import netCDF4 as nc
import numpy as np
import sys

ds=nc.Dataset('./data.nc')

print(','.join(map(str,[ds['avg_tprate'][i][0][0]*86400 for i in range(0,10)])) )
