# Joomla Scanner
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

* 2016.05.20 0.4beta > Find README.md, Find Manifes.xml, Find Index file of Components (Only if descriptive), User Agent and TimeOut on Python Request, Updated database from 587 to 656 components, Fix Cosmetics and Minor Fix.
* 2016.03.18 0.3beta > Find index file on components directory
* 2016.03.14 0.2beta > Find administrator components and file Readme, Changelog, License.
* 2016.02.12 0.1beta > Initial release

# License
GNU, version 3

