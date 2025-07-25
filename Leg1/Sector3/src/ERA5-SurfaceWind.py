import cdsapi
import sys

year=sys.argv[1]
month=sys.argv[2]
day=sys.argv[3]

north=sys.argv[4]
west=sys.argv[5]
south=sys.argv[6]
east=sys.argv[7]

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        # "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "surface_air_temperature",
        "mean_sea_level_pressure",    
        "total_precipitation",    
        "sea_surface_temperature",
        #"mean_wave_direction",
        #"mean_wave_period"
    ],
    "year": [
        year
    ],
    "month": [
        month
    ],
    "day": [
       day
    ],
    "time": [
        "00:00", "06:00", "12:00", "18:00"
    ],
    "data_format": "netcdf",
    "download_format": "zip",
    'area': [
        north, west, south, east,  # North, West, South, East (Example: parts of Europe)
    ],
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
