import xarray as xr
import netCDF4 as nc
import numpy as np

ds = xr.open_mfdataset('current*.nc',combine = 'nested', concat_dim="time")
ds.to_netcdf('currents_combined.nc')
ds=nc.Dataset('currents_combined.nc')

directions=[[(90 - np.degrees(np.arctan2(ds['vo'][:], ds['uo'][:]))) % 360][0][i][0][0][0] for i in range(0,10)]

speeds = [np.sqrt( ds['uo'][:]**2 + ds['vo'][:]**2 )[i][0][0][0] for i in range(0,10)]

dir_speed=[ f' {int(directions[i])}/{float(round(speeds[i],3))}' for i in range(0,10)]

print( ','.join(dir_speed) )