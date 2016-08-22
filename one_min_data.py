import urllib
import re
import json

#Download 1 minute stock data for AAPL by inspecting the chart element and finding a json file. 
htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/AAPL:US")
data = json.load(htmltext)

datapoints = data["data_values"]

for point in datapoints:
    print point[1]

print "The number of points is", len(datapoints)

    
