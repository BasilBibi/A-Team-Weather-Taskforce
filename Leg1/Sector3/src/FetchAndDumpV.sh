#!/bin/bash

python3 ERA5-v_component_of_wind-600hPa.py  8 31 26 -16
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py  9  7 26 -16
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py  9 14 26 -16
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py  9 21 13 -26
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py  9 28 13 -26
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py 10  5  0 -30
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py 10 12  0 -30
python3 DisplayNcFileMeans4d.py v

python3 ERA5-v_component_of_wind-600hPa.py 10 19  0 -30
python3 DisplayNcFileMeans4d.py v