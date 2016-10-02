import sys
import os
import lxml.html
import csv
from collections import defaultdict
import simplejson as json

# load files
stat_files = [fn for fn in os.listdir('fields') if fn.startswith('print_')]
countries = defaultdict(dict)

# extract field name


def get_field_name(lxmlobj):
    field_name = lx.xpath(
        '//*[@class="region"]')[0].getchildren()[0].text.replace(':', '').strip()
    return unicode(field_name)

# extract the country name and stat value


def countrystat(lxmlobj):
    country = lxmlobj.getchildren()[0].text.strip()
    stat = lxmlobj.getnext().text_content().strip()
    return unicode(country).encode('ascii', 'ignore'), unicode(stat).encode('ascii', 'ignore')

# generate the csvs
for fn in stat_files:
    with open(os.path.join('fields', fn)) as statfile:
        lx = lxml.html.fromstring(statfile.read())
        field_name = get_field_name(lx)
        fname = "".join(x for x in field_name if x.isalnum()).lower().strip() + '.csv'
        print "printing CSV for", field_name
        with open(os.path.join('stat-out', fname), 'w') as csvout:
            csvwrite = csv.writer(csvout, delimiter=',',
                                  quotechar='"', quoting=csv.QUOTE_MINIMAL)
            country_list = lx.xpath('//*[@class="fl_region"]')

            for country in country_list:
                c, stat = countrystat(country)
                csvwrite.writerow([c, stat])
                countries[c.lower()][field_name] = stat

for country in countries:
    print "printing JSON for", country
    with open(os.path.join('country-out', country.replace(' ', '_') + '.json'), 'w') as cout:
        cout.write(json.dumps(countries[country], indent=2, sort_keys=True))
