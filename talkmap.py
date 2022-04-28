#!/usr/bin/env python

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim

g = glob.glob("*.md")


geocoder = Nominatim(user_agent = 'talkmap-moshe')
location_dict = {}
location = ""
permalink = ""
title = ""


for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        def get_field(field):
            n = lines.find(field + ': "')
            if n < 2:
                return ''
            loc_start = n + len(field) + 3
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            return lines_trim[:loc_end]


        location = get_field('location')
        title = get_field('title')
        date = get_field('date')

        slug = file.rsplit('.', 1)[0]

        key = ';;'.join([slug, title, date, location])

        location_dict[key] = geocoder.geocode(location)
        print(key, "\n", location_dict[key])


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)




