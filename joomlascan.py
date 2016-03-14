#!/usr/bin/python
import sys
import httplib
import urllib2
import argparse
from urlparse import urlparse
from bs4 import BeautifulSoup

dbarray = []
https = False
url = ""

def hello():
	print "-------------------------------------------"
	print "      	 Joomla Components Scanner        "
	print "   Usage: python joomlascan.py <target>    "
	print "    Version 0.2b - Database Entries " + str(len(dbarray))
	print "         created by Andrea Draghetti       "
	print "-------------------------------------------"

def load_component():
	with open("comptotestdb.txt", "r") as f:
		for line in f:
			dbarray.append(line[:-1]) if line[-1] == "\n" else dbarray.append(line)

def check_url(url, path="/"):
	parse_url = urlparse(url)
	if parse_url.scheme == "https":
		https = True
	else:
		https = False

	if https:
		try:
			conn = httplib.HTTPSConnection(parse_url.hostname)
			conn.request("HEAD", path)
			return conn.getresponse().status
		except StandardError:
			return None
	else:
		try:
			conn = httplib.HTTPConnection(parse_url.hostname)
			conn.request("HEAD", path)
			return conn.getresponse().status
		except StandardError:
			return None

def check_readme(url, component):
	if check_url(url, "/components/" + component + "/README.txt") == 200:
		print "\t README file found \t > " + url + "/components/" + component + "/README.txt"

	if check_url(url, "/components/" + component + "/readme.txt") == 200:
		print "\t README file found \t > " + url + "/components/" + component + "/readme.txt"
		
	if check_url(url, "/administrator/components/" + component + "/README.txt") == 200:
		print "\t README file found \t > " + url + "/administrator/components/" + component + "/README.txt"

	if check_url(url, "/administrator/components/" + component + "/readme.txt") == 200:
		print "\t README file found \t > " + url + "/administrator/components/" + component + "/readme.txt"
		
def check_license(url, component):
	if check_url(url, "/components/" + component + "/LICENSE.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/components/" + component + "/LICENSE.txt"

	if check_url(url, "/components/" + component + "/license.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/components/" + component + "/license.txt"
		
	if check_url(url, "/administrator/components/" + component + "/LICENSE.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/LICENSE.txt"

	if check_url(url, "/administrator/components/" + component + "/license.txt") == 200:
		print "\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/license.txt"	
		
def check_changelog(url, component):
	if check_url(url, "/components/" + component + "/CHANGELOG.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/components/" + component + "/CHANGELOG.txt"

	if check_url(url, "/components/" + component + "/changelog.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/components/" + component + "/changelog.txt"
		
	if check_url(url, "/administrator/components/" + component + "/CHANGELOG.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/administrator/components/" + component + "/CHANGELOG.txt"

	if check_url(url, "/administrator/components/" + component + "/changelog.txt") == 200:
		print "\t CHANGELOG file found \t > " + url + "/administrator/components/" + component + "/changelog.txt"	
		

def index_of(url, path="/"):
	fullurl = url + path
	req = urllib2.Request(fullurl)
	try:
		resp = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		if e.code == 404:
			return False
		else:
			return False
	except urllib2.URLError as e:
		return False
	else:
		page = resp.read()
		soup = BeautifulSoup(page, "html.parser")
		if soup.title:
			titlepage = soup.title.string
			if (titlepage and "Index of /" in titlepage):
				return True
			else:
				return False
		else:
			return False
	
def main(argv):
	global url

	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', action='store', dest='url',
                    help='Url to be analyzed')
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
	
		print ""
	
		if check_url(url, "/robots.txt") == 200:
			print "Robots file found: \t \t > " + url + "/robots.txt"
			print ""
			
		if check_url(url, "/error_log") == 200:
			print "Error log found: \t \t > " + url + "/error_log"
			print ""
			
		
		print "Start scan..."
		print ""
	
		for i in range(len(dbarray)):
			component = dbarray[i]
	
			if check_url(url, "/index.php?option=" + component) == 200:
				print "Component found: " + component + "\t > " + url + "/index.php?option=" + component
				
				check_readme(url, component)
					
				check_license(url, component)	

				check_changelog(url, component)					
									
				if index_of(url, "/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/components/" + component + "/"
				
				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/"
			
			elif check_url(url, "/components/" + component + "/" ) == 200:
				print "Component found: " + component + "\t > " + url + "/index.php?option=" + component + "\t but possibly it is not active or protected"
				
				check_readme(url, component)
					
				check_license(url, component)	

				check_changelog(url, component)	
									
				if index_of(url, "/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/components/" + component + "/"

				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/"
										
			elif check_url(url, "/administrator/components/" + component + "/" ) == 200:
				print "Component found: " + component + "\t > " + url + "/index.php?option=" + component + "\t on the administrator components"

				check_readme(url, component)
					
				check_license(url, component)	

				check_changelog(url, component)	
				
				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/components/" + component + "/"

				if index_of(url, "/administrator/components/" + component + "/"):
					print "\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/"
							
	else:
		print "Site Down, check url please..."


if __name__ == "__main__":
	main(sys.argv[1:])
