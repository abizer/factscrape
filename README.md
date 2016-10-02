# factscrape
Data parsed into CSV (by statistic) and JSON (by country) from the CIA World Factbook

CIA data is pulled from [this zip from 2014][1].
Only [this folder][2] is used.

See `collect_stats.py` for the logic used to parse the files the `fields/` folder. 

The `stat-out` folder is composed of CSV files containing country,data pairs for every country which exposes the field given by the filename. 
The `country-out` folder is composed of JSON files representing every country and containing every field that country exposes.

The data has not been completely wrangled in order to make it more flexible for manipulation down the road.

All copyrights/trademarks belong to their owners and/or the CIA.

[1]: https://www.cia.gov/library/publications/download/download-2014/factbook.zip
[2]: https://www.cia.gov/library/publications/download/download-2014/fields.zip
