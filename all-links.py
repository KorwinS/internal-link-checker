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
	urlList.append(link['href'])

# Check for results
errorCount=0
if len(urlList)==0:
	print("No links found on page")
else:
	# Loop through url and test each one
	print("Testing all URLs")
	for i in urlList:
		conn = http.client.HTTPConnection(host)
		#headers = {'User-Agent': 'Mozilla/5.0'}
		conn.request("GET", i) # Add str(headers) into the request to add the useragent
		res = conn.getresponse()
		print(res.status,res.reason," : ",i)
		if res.status > 399:
			errorCount=errorCount+1

# Report Error responses
print("Number of Errors: ",errorCount)