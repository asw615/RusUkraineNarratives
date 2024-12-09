#!/usr/bin/env python
"""
This script downloads article information of one URL. The results are stored in JSON-files in a sub-folder.
You need to adapt the variables url and basepath in order to use the script.
"""

import json

from newsplease import NewsPlease

url = 'https://www.dr.dk/nyheder/politik/jobskifte-lukker-sag-hovedperson-i-minksag'
basepath = '/Users/sorenmeiner/Documents/data'

article = NewsPlease.from_url(url)

with open('hallo.json', 'w', ) as outfile:
    json.dump(article, outfile, indent=4, sort_keys=True, default=str)
