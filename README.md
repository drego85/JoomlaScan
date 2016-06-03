# Joomla Scan
A free and open source software to find the components installed in Joomla CMS, built out of the ashes of Joomscan.

# Features
* Scanning the Joomla CMS sites in search of components/extensions (database of more than 600 components);
* Locate the browsable folders of component (Index of ...);
* Locate the components disabled or protected
* Locate each file useful to identify the version of a components (Readme, Manifest, License, Changelog)
* Locate the robots.txt file or error_log file
* Supports HTTP or HTTPS connections
* Connection timeout

# Next Features
* Multi Thread (It is the main work to be done, with more than 600 components the research has become slow.)
* Locate the version of Joomla CMS
* Find Module
* Customized User Agent or Random Agent
* The user can change the connection timeout
* A database of vulnerable components

# Usage

$ python joomlascan.py -u http://www.targetsite.com

# Screenshot

![alt Screenshot 0.4b](http://cloud.draghetti.it/Rehost_Image/Joomla_Scan_0.4b.png)

# Requirements
* Python
* beautifulsoup4 (To install this library from terminal type: $ sudo easy_install beautifulsoup4 or $ sudo pip install beautifulsoup4)

# Changelog

joomlascan (0.5) testing; urgency=medium

	* Debianize source code
	* Create Makefile
	* Test dependencies on Debian and Parrot
	* Beautify changelog
	* Import joomlascan into Parrot repository

 -- Lorenzo "Palinuro" Faletra <eclipse@parrotsec.org>  Fri, 03 Jun 2016 16:49:38 +0200

joomlascan (0.4) experimental; urgency=medium

	* Find README.md
	* Find Manifes.xml
	* Find Index file of Components (Only if descriptive)
	* User Agent and TimeOut on Python Request
	* Updated database from 587 to 656 components
	* Fix Cosmetics and Minor Fix.

 -- Andrea Draghetti <info@andreadraghetti.it>  20 Apr 2016
 
joomlascan (0.3) experimental; urgency=medium

	* Find index file on components directory

 -- Andrea Draghetti <info@andreadraghetti.it>  18 Mar 2016
 
joomlascan (0.2) experimental; urgency=medium

	* Find administrator components and file Readme, Changelog, License.

 -- Andrea Draghetti <info@andreadraghetti.it>  14 Mar 2016

joomlascan (0.1) experimental; urgency=medium

	* Initial release

 -- Andrea Draghetti <info@andreadraghetti.it>  12 Feb 2016

# License
GNU, version 3



