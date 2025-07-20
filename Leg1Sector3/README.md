#Leg1 Sector3

This sector was divided into 3 main loactions for data collection as shown in this diagram.

![alt text](Leg1Sector3Location.jpeg "Leg1 Sector3")

### Dates and coordinates for data extracts
The following years were extracted 
2015 to 2024 for the following months and locations 

| Month - Day | Coordinates |
| :---------- | :---------- |
| 08-31       | N26 W16    |
| 09-07       | N26 W16 |
| 09-14       | N26 W16 | 
| 09-21       | N13 W26 |
| 09-28       | N13 W26 |
| 10-05       | N0 W30  |
| 10-12       | N0 W30 |
| 10-19       | N0 W30 |

### Data Metrics and Scripts

| Data Metric | Source | Variables | Top Level Script |
| :---------- | :----- | :-------- | ---------------- |
| Windspeed/Direction at 10m | [Copernicus ERA5 hourly data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | 10m_v_component_of_wind 10m_u_component_of_wind | FetchAndDump10MWind.sh |
| Windspeed/Direction at 600hPa | [Copernicus ERA5 hourly data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | v_component_of_wind u_component_of_wind 10m_v_component_of_wind | FetchAndDump600hPaWind.sh |
| Surface Air Temperature | [Copernicus ERA5 hourly data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | 2m_temperature | FetchAndDumpT2m.sh |
| Mean Sea Level Pressure| [Copernicus ERA5 hourly data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | mean_sea_level_pressure | FetchAndDumpMSL.sh |
| Precipitation | [Copernicus ERA5 hourly data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) | mean_total_precipitation_rate | FetchAndDump-avg-tprate.sh |
| Current Direction/Speed | [Copernicus Marine CMEMS](https://documentation.marine.copernicus.eu/PUM/CMEMS-GLO-PUM-001-030.pdf) cmems_mod_glo_phy_my_0.083deg_P1D-m cmems_mod_glo_phy_myint_0.083deg_P1D-m | vo uo | FetchAndDump-CopMarCurrents.sh |



