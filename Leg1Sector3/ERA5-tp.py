import cdsapi
import sys

month=sys.argv[1]
day=sys.argv[2]
north=sys.argv[3]
south=north#+'.01'
west=sys.argv[4]
east=west#+'.01'

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "mean_total_precipitation_rate"
    ],
    "year": [
        2015, 2016, 2017, 2018, 2019, 
        2020, 2021, 2022, 2023, 2024
    ],
    "month": [ month ],
    "day": [ day ],
    #"time": [ "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00",
    #          "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", 
    #          "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", 
    #          "19:00", "20:00", "21:00", "22:00", "23:00"],
    "data_format": "netcdf",
    'area': [
        north, west, south, east,  # North, West, South, East (Example: parts of Europe)
    ],
}

client = cdsapi.Client()
client.retrieve(dataset, request,'data.nc')
