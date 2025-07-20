import xarray as xr
import netCDF4 as nc
import numpy as np

ds = xr.open_mfdataset('waves*.nc',combine = 'nested', concat_dim="time")
ds.to_netcdf('waves_combined.nc')
ds=nc.Dataset('waves_combined.nc')


wave_period=[float(round(ds['VTM10'][i][0][0],3)) for i in range(0,10)]
print( ','.join(map(str,wave_period)))


wave_heights=[float(round(ds['VHM0'][i][0][0],3)) for i in range(0,10)]
print( ','.join(map(str,wave_heights)))
