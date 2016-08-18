import urllib
import re

#Scraping Apple's current stock price
htmltext_aapl = urllib.urlopen("https://www.google.com/finance?q=AAPL").read()
regex = '<span id="ref_[^.]*_l">(.+?)</span>'
pattern = re.compile(regex)
results = re.findall(pattern, htmltext_aapl)
print results

#Scraping Google's closing stock price using getprices
#getprices'url was obtained from observing the Networks tab on clicking stock price's inspect elment  
htmltext_goog = urllib.urlopen("https://www.google.com/finance/getprices?q=GOOG&x=NASD&i=120&p=40Y&f=c&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg").read();
print htmltext_goog.split()[len(htmltext_goog.split()) - 1]
