#!/usr/bin/python
import sys
import httplib
import requests
import argparse
from bs4 import BeautifulSoup

dbarray = []
url = ""
useragentdesktop = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)", "Accept-Language": "it"}
timeoutconnection = 5

def hello():
	print "-------------------------------------------"
	print "      	     Joomla Scan                  "
	print "   Usage: python joomlascan.py <target>    "
	print "    Version 0.4b - Database Entries " + str(len(dbarray))
	print "         created by Andrea Draghetti       "
	print "-------------------------------------------"

def load_component():
	with open("comptotestdb.txt", "r") as f:
		for line in f:
			dbarray.append(line[:-1]) if line[-1] == "\n" else dbarray.append(line)

def check_url(url, path="/"):

	fullurl = url + path
	try:
		conn = requests.get(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
		return conn.status_code
	except StandardError:
		return None
		
def check_url_head_content_length(url, path="/"):

	fullurl = url + path
	try:
		conn = requests.head(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
		return conn.headers["content-length"]
	except StandardError:
		return None

def check_readme(url, component):
	if check_url(url, "/components/" + component + "/README.txt") == 200:
		print "\t README file found \t > " + url + "/components/" + component + "/README.txt"

	if check_url(url, "/components/" + component + "/readme.txt") == 200:
		print "\t README file found \t > " + url + "/components/" + component + "/readme.txt"
		
	if check_url(url, "/components/" + component + "/README.md") == 200:
		print "\t README file found \t > " + url + "/components/" + component + "/README.md"
	
	if check_url(url, "/components/" + component + "/readme.md") == 200:
		print "\t README file found \t > " + url + "/components/" + component + "/readme.md"		
		
	if check_url(url, "/administrator/components/" + component + "/README.txt") == 200:
		print "\t README file found \t > " + url + "/administrator/components/" + component + "/README.txt"

	if check_url(url, "/administrator/components/" + component + "/readme.txt") == 200:
		print "\t README file found \t > " + url + "/administrator/components/" + component + "/readme.txt"
		
	if check_url(url, "/administrator/components/" + component + "/README.md") == 200:
		print "\t README file found \t > " + url + "/administrator/components/" + component + "/README.md"

	if check_url(url, "/administrator/components/" + component + "/readme.md") == 200:
		print "\t README file found \t > " + url + "/administrator/components/" + component + "/readme.md"
		
def check_license(url, component):
	if check_url(url, "/components/" + component + "/LICENSE.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/components/" + component + "/LICENSE.txt"

	if check_url(url, "/components/" + component + "/license.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/components/" + component + "/license.txt"
		
	if check_url(url, "/administrator/components/" + component + "/LICENSE.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/LICENSE.txt"

	if check_url(url, "/administrator/components/" + component + "/license.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/license.txt"	
	
        if check_url(url, "/components/" + component + "/" + component[4:] + ".xml") == 200:
            print "\t LICENSE file found \t > " + url + "/components/" + component + "/" + component[4:] + ".xml"
		
        if check_url(url, "/administrator/components/" + component + "/" + component[4:] + ".xml") == 200:
            print "\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/" + component[4:] + ".xml"
		
def check_changelog(url, component):
	if check_url(url, "/components/" + component + "/CHANGELOG.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/components/" + component + "/CHANGELOG.txt"

	if check_url(url, "/components/" + component + "/changelog.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/components/" + component + "/changelog.txt"
		
	if check_url(url, "/administrator/components/" + component + "/CHANGELOG.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/administrator/components/" + component + "/CHANGELOG.txt"

	if check_url(url, "/administrator/components/" + component + "/changelog.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/administrator/components/" + component + "/changelog.txt"	
		
def check_mainfest(url, component):
	if check_url(url, "/components/" + component + "/MANIFEST.xml") == 200:
		print "\t MANIFEST file found \t > " + url + "/components/" + component + "/MANIFEST.xml"

	if check_url(url, "/components/" + component + "/manifest.xml") == 200:
		print "\t MANIFEST file found \t > " + url + "/components/" + component + "/manifest.xml"
		
	if check_url(url, "/administrator/components/" + component + "/MANIFEST.xml") == 200:
		print "\t MANIFEST file found \t > " + url + "/administrator/components/" + component + "/MANIFEST.xml"

	if check_url(url, "/administrator/components/" + component + "/manifest.xml") == 200:
		print "\t MANIFEST file found \t > " + url + "/administrator/components/" + component + "/manifest.xml"		
		
def check_index(url, component):
	if check_url_head_content_length(url, "/components/" + component + "/index.htm") == 200 and check_url_head(url, "/components/" + component + "/index.htm") > 1000:
		print "\t INDEX file descriptive found \t > " + url + "/components/" + component + "/index.htm"

	if check_url_head_content_length(url, "/components/" + component + "/index.html") == 200 and check_url_head(url, "/components/" + component + "/index.html") > 1000:
		print "\t INDEX file descriptive found \t > " + url + "/components/" + component + "/index.html"
		
	if check_url_head_content_length(url, "/administrator/components/" + component + "/INDEX.htm") == 200 and check_url_head(url, "/administrator/components/" + component + "/INDEX.htm") > 1000:
		print "\t INDEX file descriptive found \t > " + url + "/administrator/components/" + component + "/INDEX.htm"

	if check_url_head_content_length(url, "/administrator/components/" + component + "/INDEX.html") == 200 and check_url_head(url, "/administrator/components/" + component + "/INDEX.html") > 1000:
		print "\t INDEX file descriptive found \t > " + url + "/administrator/components/" + component + "/INDEX.html"

def index_of(url, path="/"):
	fullurl = url + path
	try:
		page = requests.get(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
		soup = BeautifulSoup(page.text, "html.parser")
		if soup.title:
			titlepage = soup.title.string
			if (titlepage and "Index of /" in titlepage):
				return True
			else:
				return False
		else:
			return False
	except:
		return False
	
def main(argv):
	global url

	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', action='store', dest='url', help='Url to be analyzed')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1b')

	results = parser.parse_args()

	if results.url:
		url = results.url
		if url[:8] != "https://" and url[:7] != "http://":
			print("You must insert http:// or https:// procotol")
			sys.exit(1)
	else:
		print "url is required"
		print ""
		parser.parse_args(['-h'])
		sys.exit(1)

	load_component()
	
	hello()
	
	if check_url(url) == 200:
	
		print "Check Site..."
	
		if check_url(url, "/robots.txt") == 200:
			print "Robots file found: \t \t > " + url + "/robots.txt"
		else:
			print "No Robots file found"
			
		if check_url(url, "/error_log") == 200:
			print "Error log found: \t \t > " + url + "/error_log"
		else:
			print "No Error Log found"
		
		print ""
		print "Start scan..."
	
		for i in range(len(dbarray)):
			component = dbarray[i]
		
			if check_url(url, "/index.php?option=" + component) == 200:
				print "Component found: " + component + "\t > " + url + "/index.php?option=" + component
				
				check_readme(url, component)
					
				check_license(url, component)	

				check_changelog(url, component)
			
				check_mainfest(url, component)
				
				check_index(url, component)			
									
				if index_of(url, "/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/components/" + component + "/"
				
				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/"
			
			elif check_url(url, "/components/" + component + "/" ) == 200:
				print "Component found: " + component + "\t > " + url + "/index.php?option=" + component
				print "\t But possibly it is not active or protected"
				
				check_readme(url, component)
					
				check_license(url, component)	

				check_changelog(url, component)
			
				check_mainfest(url, component)
				
				check_index(url, component)		
				
				if index_of(url, "/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/components/" + component + "/"

				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/"
										
			elif check_url(url, "/administrator/components/" + component + "/" ) == 200:
				print "Component found: " + component + "\t > " + url + "/index.php?option=" + component
				print "\t On the administrator components"

				check_readme(url, component)
					
				check_license(url, component)	

				check_changelog(url, component)
			
				check_mainfest(url, component)
				
				check_index(url, component)
				
				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/components/" + component + "/"

				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/"
							
	else:
		print "Site Down, check url please..."


if __name__ == "__main__":
	main(sys.argv[1:])
