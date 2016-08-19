# -*- coding: utf-8 -*-
import urllib
import re
import json

#Retrieve last price of AAPl stock from Bloomberg's website, interpreting json response
htmltext = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US")
data = json.load(htmltext)
print data["last_price"]
