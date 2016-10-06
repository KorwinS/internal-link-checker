import http.client
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer

# Get the hostname
host = input("Host name to test (like www.example.com)?: ")
url = "http://"+host
page = urllib.request.urlopen(url)
navlinks = SoupStrainer('a', {'class': ''})
soup = BeautifulSoup(page, "html.parser", parse_only=navlinks)
links = soup.findAll('a')

# Create an Empty List for the list of URLs
urlList = []

# Loop through the links found
for link in links:
    if link['href'].startswith("/"): #filter internal links
        urlList.append(link['href'])

# Check for results
if len(urlList)==0:
	print("No internal links found on page")
else:
	# Loop through url and test each one
	print("Testing internal URLs")
	count=0
	for i in urlList:
		conn = http.client.HTTPConnection(host)
		conn.request("GET", i)
		res = conn.getresponse()
		print(res.status,res.reason," : ",i)