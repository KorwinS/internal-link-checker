import urllib.request
import socket
from bs4 import BeautifulSoup, SoupStrainer

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)

errorCount=0

# Get the hostname
host = input("Host name to test (like www.example.com)?: ")
url = "http://"+host

# Open the page
page = urllib.request.urlopen(url)

# Filter for <a> tags
navlinks = SoupStrainer('a', {'class': ''})
soup = BeautifulSoup(page, "html.parser", parse_only=navlinks)
links = soup.findAll('a')

# Loop through the links found, check for dupes, add to list
urlList = []
for link in links:
	if link['href'] not in urlList:
		urlList.append(link['href'])

# Function to Handle Error Results
def printErrorCode(x):
	print(e.code," : ",x)
	global errorCount
	errorCount=errorCount+1

# Check for links in list
if len(urlList)==0:
	print("No links found on page")
else:
	# Loop through url and test each one
	print("Testing all URLs")
	for i in urlList:
		if i.startswith('http'): 
			# External Links 
			try:
				fullURL=urllib.request.urlopen(i)
			except urllib.error.URLError as e:
				printErrorCode(i)
		else: 
			# Internal Links
			try:
				fullURL=urllib.request.urlopen(url+i)
			except urllib.error.URLError as e:
				printErrorCode(i)
		print(fullURL.getcode()," : ",i)

# Report Error responses
print("Number of Errors: ",errorCount)