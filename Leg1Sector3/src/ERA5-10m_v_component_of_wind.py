import cdsapi
import sys

month=sys.argv[1]
day=sys.argv[2]
north=sys.argv[3]
south=north
west=sys.argv[4]
east=west

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "10m_v_component_of_wind", "10m_u_component_of_wind"
    ],
    "year": [
        2015, 2016, 2017, 2018, 2019, 
        2020, 2021, 2022, 2023, 2024
    ],
    "month": [ month ],
    "day": [ day ],
    "data_format": "netcdf",
    'area': [
        north, west, south, east,  # North, West, South, East (Example: parts of Europe)
    ],
}

client = cdsapi.Client()
client.retrieve(dataset, request,'data.nc')
