#!/usr/bin/env python3
import sys
import requests
import argparse
from bs4 import BeautifulSoup
import threading
import time
from colorama import init, Fore
from tqdm import tqdm

init(autoreset=True)

dbarray = []
url = ""
timeoutconnection = 5
session = requests.Session()
aliversion = "1.0 Ready"

def hello():
    print(Fore.GREEN + "-------------------------------------------")
    print("             Joomla Scan                  ")
    print("   Usage: python joomlascan.py <target>    ")
    print("    Version " + aliversion + " - Updates " + str(len(dbarray)))
    print("created by Andrea Draghetti , Edited By AliElTop")
    print("-------------------------------------------")

def load_component():
    with open("comptotestdb.txt", "r") as f:
        for line in f:
            dbarray.append(line.strip())

def check_url(url, headers, path="/"):
    full_url = url + path
    try:
        conn = requests.get(full_url, headers=headers, timeout=timeoutconnection, verify=False)
        if conn.headers.get("content-length") != "0":
            return conn.status_code
        else:
            return 404
    except Exception:
        return None

def find_file(url, component, filenames):
    for filename in filenames:
        if check_url(url, f"/components/{component}/{filename}") is not None:
            return filename
        if check_url(url, f"/administrator/components/{component}/{filename}") is not None:
            return filename
    return None

def check_readme(url, component):
    filenames = ["README.txt", "readme.txt", "README.md", "readme.md"]
    found_file = find_file(url, component, filenames)
    if found_file:
        return f"{Fore.GREEN}\t {found_file.upper()} file found \t > {url}/components/{component}/{found_file}\n"
    return ""

def check_license(url, component):
    filenames = ["LICENSE.txt", "license.txt", f"{component[4:]}.xml"]
    found_file = find_file(url, component, filenames)
    if found_file:
        return f"{Fore.GREEN}\t {found_file.upper()} file found \t > {url}/components/{component}/{found_file}\n"
    return ""

def check_changelog(url, component):
    filenames = ["CHANGELOG.txt", "changelog.txt"]
    found_file = find_file(url, component, filenames)
    if found_file:
        return f"{Fore.GREEN}\t {found_file.upper()} file found \t > {url}/components/{component}/{found_file}\n"
    return ""

def check_manifest(url, component):
    filenames = ["MANIFEST.xml", "manifest.xml"]
    found_file = find_file(url, component, filenames)
    if found_file:
        return f"{Fore.GREEN}\t {found_file.upper()} file found \t > {url}/components/{component}/{found_file}\n"
    return ""

def check_index(url, component):
    filenames = ["index.htm", "index.html"]
    for filename in filenames:
        full_url = url + f"/components/{component}/{filename}"
        try:
            response = session.head(full_url, timeout=timeoutconnection)
            if response.status_code == 200 and int(response.headers.get("content-length", 0)) > 1000:
                return f"{Fore.GREEN}\t {filename.upper()} file descriptive found \t > {full_url}\n"
        except requests.RequestException:
            pass
    return ""

def index_of(url, path="/"):
    full_url = url + path
    try:
        response = session.get(full_url, timeout=timeoutconnection)
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.title and "Index of /" in soup.title.string:
            return True
    except requests.RequestException:
        pass
    return False

def scanner(url, component):
    result = ""

    if check_url(url, "/index.php?option=" + component) is not None:
        result += f"{Fore.GREEN}Component found: {component}\t > {url}/index.php?option={component}\n"
    else:
        result += f"{Fore.YELLOW}No component found: {component} at {url}/index.php?option={component}\n"

    result += check_readme(url, component)
    result += check_license(url, component)
    result += check_changelog(url, component)
    result += check_manifest(url, component)
    result += check_index(url, component)

    if index_of(url, "/components/" + component + "/"):
        result += f"{Fore.CYAN}\t Explorable Directory \t > {url}/components/{component}/\n"

    if index_of(url, "/administrator/components/" + component + "/"):
        result += f"{Fore.CYAN}\t Explorable Directory \t > {url}/administrator/components/{component}/\n"

    if result:
        print(result)

    pool.release()

def main(argv):
    useragentdesktop = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Accept-Language": "it"
    }

    load_component()

    hello()

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url", action="store", dest="url", help="The Joomla URL/domain to scan.")
        parser.add_argument("-t", "--threads", action="store", dest="threads",
                            help="The number of threads to use when multi-threading requests (default: 10).")
        parser.add_argument("-v", "--version", action="version", version="%(prog)s " + aliversion)

        arguments = parser.parse_args()
    except:
        sys.exit(1)

    if arguments.url:
        url = arguments.url
        if url[:8] != "https://" and url[:7] != "http://":
            print("You must insert http:// or https:// protocol\n")
            sys.exit(1)

        if url[-1:] == "/":
            url = url[:-1]
    else:
        print("")
        parser.parse_args(["-h"])
        sys.exit(1)

    concurrent_threads = 10
    global pool

    if arguments.threads and arguments.threads.isdigit():
        concurrent_threads = int(arguments.threads)
        pool = threading.BoundedSemaphore(concurrent_threads)
    else:
        pool = threading.BoundedSemaphore(concurrent_threads)

    if check_url(url, useragentdesktop) is not None:
        if check_url(url, useragentdesktop, "/robots.txt") is not None:
            print(Fore.GREEN + f"Robots file found: \t \t > {url}/robots.txt")
        else:
            print(Fore.YELLOW + "No Robots file found")

        if check_url(url, useragentdesktop, "/error_log") is not None:
            print(Fore.GREEN + f"Error log found: \t \t > {url}/error_log")
        else:
            print(Fore.YELLOW + "No Error Log found")

        print(Fore.CYAN + "\nStart scan...with %d concurrent threads!" % concurrent_threads)

        results = []

        for component in tqdm(dbarray, desc="Scanning Components"):
            pool.acquire(blocking=True)
            t = threading.Thread(target=scanner, args=(url, component,))
            t.start()
            results.append(t)

        for t in tqdm(results, desc="Waiting for Threads"):
            t.join()

        print(Fore.CYAN + "End Scanner")
    else:
        print(Fore.RED + "Site Down, check URL please...")

if __name__ == "__main__":
    main(sys.argv[1:])
