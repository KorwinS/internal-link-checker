import urllib.request
import socket
from bs4 import BeautifulSoup, SoupStrainer

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)

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
		if i.startswith('http'): 
			# External Links
			fullURL=urllib.request.urlopen(i)
			print(fullURL.getcode()," : ",i)
			if fullURL.getcode() > 399:
				errorCount=errorCount+1
		else: 
			# Internal Links
			try:
				fullURL=urllib.request.urlopen(url+i)
			except urllib.error.URLError as e:
				print(e.code," : ",i)
				errorCount=errorCount+1
			print(fullURL.getcode()," : ",i)
			if fullURL.getcode() > 399:
				errorCount=errorCount+1

# Report Error responses
print("Number of Errors: ",errorCount)