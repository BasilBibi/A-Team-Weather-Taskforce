import os
import copernicusmarine as cpm
import xarray as xr
import numpy as np
from  datetime import datetime
import sys

month=sys.argv[1]
day=sys.argv[2]
north=float(sys.argv[3])
south=north
west=float(sys.argv[4])
east=west

os.environ['COPERNICUSMARINE_SERVICE_USERNAME'] = 'bbibi'
os.environ['COPERNICUSMARINE_SERVICE_PASSWORD'] = 'MPF1whb@ntj0qpf9ceh'

cpm.login(username=os.environ['COPERNICUSMARINE_SERVICE_USERNAME'],
         password=os.environ['COPERNICUSMARINE_SERVICE_PASSWORD'])

currents_ds_0 = "cmems_mod_glo_phy_my_0.083deg_P1D-m"
currents_ds_1 = "cmems_mod_glo_phy_myint_0.083deg_P1D-m"

for dt_str in [
    f'2015-{month}-{day}', 
    f'2016-{month}-{day}',
    f'2017-{month}-{day}',
    f'2018-{month}-{day}',
    f'2019-{month}-{day}',
    f'2020-{month}-{day}'
    ] :
    print(dt_str)
    cpm.subset(
        dataset_id=currents_ds_0,
        start_datetime=dt_str,
        end_datetime=dt_str,
        minimum_longitude=east,
        maximum_longitude=west,
        minimum_latitude=north,
        maximum_latitude=south,
        minimum_depth=0,
        maximum_depth=1,
        output_filename = "currents.nc"
    )

for dt_str in [
    f'2021-{month}-{day}',
    f'2022-{month}-{day}',
    f'2023-{month}-{day}',
    f'2024-{month}-{day}'
    ] :
    print(dt_str)
    cpm.subset(
        dataset_id=currents_ds_1,
        start_datetime=dt_str,
        end_datetime=dt_str,
        minimum_longitude=east,
        maximum_longitude=west,
        minimum_latitude=north,
        maximum_latitude=south,
        minimum_depth=0,
        maximum_depth=1,
        output_filename = "currents.nc"
    )