#!/bin/bash

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  08 31 26 -16
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  09 07 26 -16
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  09 14 26 -16
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  09 21 13 -26
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  09 28 13 -26
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  10 05  0 -30
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  10 12  0 -30
python3 ./CombineAndDisplayCurrentData.py
echo ""

rm currents*.nc
python3 ./GetCopernucusMarineDataVo.py  10 19  0 -30
python3 ./CombineAndDisplayCurrentData.py
echo ""