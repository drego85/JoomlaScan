# Joomla Components Scanner
A free and open source software to find the components installed in Joomla CMS, built out of the ashes of Joomscan.

# Features
* Scanning the Joomla CMS sites in search of components/extensions (database of more than 500 components);
* Locate the browsable folders of component (Index of ...);
* Locate the components disabled or protected
* Locate the robots.txt file or error_log file
* Supports HTTP or HTTPS connections

# Next Features
* Locate the version of Joomla CMS
* Customized User Agent
* Set a connection timeout
* A database of vulnerable components

# Usage

$ python joomlascan.py -u http://www.targetsite.com

# Screenshot

![alt Screenshot 0.2b](http://cloud.draghetti.it/Rehost_Image/Joomla_Components_Scanner_0.2b.png)
![alt Screenshot 0.1b](http://cloud.draghetti.it/Rehost_Image/Joomla_Components_Scanner_0.1b.png)

# Requirements
* Python
* beautifulsoup4 (To install this library from terminal type: $ sudo easy_install beautifulsoup4)

# Changelog

* 2016.03.14 0.2beta >  Find administrator components and file Readme, Changelog, License.
* 2016.02.12 0.1beta > Initial release

# License
GNU, version 3

