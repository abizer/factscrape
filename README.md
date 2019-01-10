# factscrape
Data from the CIA World Factbook "parsed" into JSON, organized by country and statistic.

CIA data is pulled from [this zip from 2017][1].
Only [this folder][2] is used.

`collect_stats.py` contains the code that attempts to turn the HTML in the `fields`
folder into some semblance of JSON.

The by-statistic and by-country folders contain JSON blobs with information organized
according to the name of the respective folder.

The data has not been completely wrangled for various reasons, not the least of which
is the utterly awful format the CIA provides it in.

All copyrights/trademarks belong to their owners and/or the CIA.

[1]: https://www.cia.gov/library/publications/download/download-2017/factbook.zip
[2]: https://www.cia.gov/library/publications/download/download-2017/fields.zip
