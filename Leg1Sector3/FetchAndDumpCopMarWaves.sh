#!/bin/bash

rm waves*.nc
python3 GetCopMarWaves.py  8 31 26 -16
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py  9  7 26 -16
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py  9 14 26 -16
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py  9 21 13 -26
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py  9 28 13 -26
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py 10  5  0 -30
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py 10 12  0 -30
python3 CombineAndDisplayWaveData.py

rm waves*.nc
python3 GetCopMarWaves.py 10 19  0 -30
python3 CombineAndDisplayWaveData.py

rm waves*.nc