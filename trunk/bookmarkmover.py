# DD tag is a user comment
# DT tag is the actual bookmark item
# TAGS are inside the anchor
#
# Example from input:
# <dt>
#  <a href="http://www.blockrocker.com/" add_date="1135704152" private="0" tags="googlemaps,craigslist,amazon">
#   BlockRocker
#  </a>
# </dt>
# <dd>
#  Wow this rocks! GoogleMaps + Craigslist + Amazon + IP Localization + RSS = BlockRocker.com
# </dd>
import re
import sys
import urllib2

from BeautifulSoup import BeautifulSoup

google_bookmarks = {}
sig = "VTTEmBUGM-KpQraF7BnLnw"
form_url = "https://www.google.com/bookmarks/mark"

delicious_file = open(sys.argv[1], 'r').readlines()

# This counter is used for goole_bookmarks keys
count = [0]
def counter():
    count[0] += 1

for line in temp_file:
    soup = BeautifulSoup(line)
    counter()
    if re.search("<DT>", line):
        anchor = soup.findAll('a', href=True)
        google_bookmarks[count[0]] = {'labels': anchor[0]['tags'],
            'bkmk': anchor[0]['href'], 'title': anchor[0].string}
    elif re.search("<DD>", line):
        last_count = count[0] - 1
        anchor = soup.findAll('dd')
        google_bookmarks[last_count]['annotation'] = anchor[0].string

