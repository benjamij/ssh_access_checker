import sys
import re
import requests
# import matplotlib
# from mpl_toolkits.basemap import Basemap
# import numpy as np
# import matplotlib.pyplot as plt

__author__ = 'Benjamin Jakobus'

# This script extracts IP addresses from log files, obtains their geolocation
# and then plots this on a map.
#
# Usage: ssh_access_check.py <location of log file>
# Output: map.png in the working directory.

# Default is the system's auth log
log_file = '/var/log/auth.log'

# Check if user wants to use a custom location
for arg in sys.argv:
    log_file = arg

# Read contents of log file
content = []
with open(log_file) as f:
    content = f.readlines()

# Extract IP addresses
ip_addresses = []
for line in content:
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
    if not ip:
        continue
    ip_addresses.append(ip[0])
    print('Connection from: ' + str(ip[0]))

# For each IP address, obtain GeoLocation:
locations = []
for ip_address in ip_addresses:
    r = requests.get('http://freegeoip.net/csv/' + str(ip_address))
    print r.text
    items = r.text.split(',')
    locations.append((items[len(items) - 3], items[len(items) - 2]))

# # Setup map
# m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
#             llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
# m.drawcoastlines()
# m.fillcontinents(color='coral',lake_color='aqua')
# # draw parallels and meridians.
# m.drawparallels(np.arange(-90.,91.,30.))
# m.drawmeridians(np.arange(-180.,181.,60.))
# m.drawmapboundary(fill_color='aqua')
# plt.title("SSH Access Attempts")
#
# for location in locations:
#     # lat,long = location[0], location[1]
#     x,y = map(location[0], location[1])
#     map.plot(x, y, 'bo', markersize=24)
#
# plt.show()
