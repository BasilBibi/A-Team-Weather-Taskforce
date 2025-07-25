import netCDF4 as nc
import numpy as np
import sys

ds=nc.Dataset('./data.nc')

directions=[[(270 - np.rad2deg(np.arctan2(ds['v10'][:], ds['u10'][:]))) % 360][0][i][0][0] for i in range(0,10)]

speeds = [np.sqrt( ds['u10'][:]**2 + ds['v10'][:]**2 )[i][0][0] for i in range(0,10)]

dir_speed=[ f' {int(directions[i])}/{int(speeds[i])}' for i in range(0,10)]

print( ','.join(dir_speed) )