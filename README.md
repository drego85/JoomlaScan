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
* Locate the version of Joomla CMS
* Find Module
* Customized User Agent and Random Agent
* The user can change the connection timeout
* A database of vulnerable components

# Usage

usage: python joomlascan.py [-h] [-u URL] [-t THREADS] [-v]

optional arguments:

    -h, --help              show this help message and exit
 
    -u URL, --url URL       The Joomla URL/domain to scan.
    -t THREADS, --threads   THREADS
                            The number of threads to use when multi-threading
                            requests (default: 10).
    -v, --version           show program's version number and exit

# Screenshot

![alt Screenshot 0.4b](http://cloud.draghetti.it/Rehost_Image/Joomla_Scan_0.4b.png)

# Requirements
* Python
* beautifulsoup4 (To install this library from terminal type: $ sudo easy_install beautifulsoup4 or $ sudo pip install beautifulsoup4)

# Changelog

* 2016.12.12 0.5beta > Implementation of the Multi Thread, Updated database from 656 to 686 components, Fix Cosmetics and Minor Fix.
* 2016.05.20 0.4beta > Find README.md, Find Manifes.xml, Find Index file of Components (Only if descriptive), User Agent and TimeOut on Python Request, Updated database from 587 to 656 components, Fix Cosmetics and Minor Fix.
* 2016.03.18 0.3beta > Find index file on components directory
* 2016.03.14 0.2beta > Find administrator components and file Readme, Changelog, License.
* 2016.02.12 0.1beta > Initial release

# License
GNU, version 3

