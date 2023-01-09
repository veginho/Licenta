import urllib

import requests
import socket
import subprocess
import os
import requests
from bs4 import BeautifulSoup
import hashlib
from tqdm import tqdm
import json


def calculate_hashes(website_link):
    with urllib.request.urlopen(website_link) as response:
        html = response.read()
    # Parse the HTML content
    soup = BeautifulSoup(html, "html.parser")
    html_string = soup.prettify()
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(html_string.encode())
    hash_hex = hash_sha256.hexdigest()
    print("The hash of the webiste is: "+hash_hex)
    req = requests.get(website_link)
    soup = BeautifulSoup(req.text, "html.parser")
    js_files = soup.find_all("script", {"src": True})
    # Find all the CSS files
    css_files = soup.find_all("link", {"rel": "stylesheet"})
    # print("CSS files")
    # print(css_files)
    for file in js_files + css_files:
        # Download the file
        file_url = file["src"] if file.name == "script" else file["href"]
        #print(file)
        urllib.request.urlretrieve(file_url, file_url.split("/")[-1])
        hash_sha256.update(file_url.encode())
        hash_hex = hash_sha256.hexdigest()
        print("The hash of the file is "+hash_hex)



def get_links(website_link):
    #url = "https://en.wikipedia.org/wiki/Algorithm"
    req = requests.get(website_link)
    soup = BeautifulSoup(req.text, "html.parser")
    print("The href links are :")
    for link in soup.find_all('a'):
       print(link.get('href'))
    js_files = soup.find_all("script", {"src": True})
    if len(js_files)==0:
        print("No external JavaScript files were found")
    # Find all the CSS files
    css_files = soup.find_all("link", {"rel": "stylesheet"})
    print("CSS files")
    print(css_files)




def detect_dns_hijacking(url):
    # Get the IP address for the domain name
    url = url.split('//')
    #print(url)
    try:
        ip_address = socket.gethostbyname(url[1])
        print(ip_address)
    except socket.gaierror:
        print("Error: Could not resolve domain name.")
        return
    dns_server = socket.gethostbyname(url[1])  # Get the DNS server for the domain name
    # print(dns_server)
    # Check if the DNS server is the same as the IP address
    if ip_address == dns_server:
        print("DNS hijacking not detected.")
    else:
        print("DNS hijacking detected!")




def discover_subdirectories(url):
    # Use Gobuster to discover subdirectories
    str = "gobuster -e -u " + url + " -w /usr/share/wordlists/common.txt"
    print(str)
    os.system(str)
    # subdirectories = subprocess.run(["gobuster", "-e ", "-u ", "https://mta.ro/", "-w ", "/usr/share/wordlists/common.txt"],capture_output=True).stdout

    # Print the subdirectories
    # print("Subdirectories:")
    # print(subdirectories.decode())


# deci teoretic un actor care intra pe aplicatie ar insera un link sa zicem si s-ar descarca acest fisier
# acum urmatorul pas ar fi aplicarea metodei 2-gram peste acest fisier

def main():
    website = input("Enter website:")
    get_links(website)
    calculate_hashes(website)
    detect_dns_hijacking(website)



if __name__ == "__main__":
    main()
