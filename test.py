import requests
import socket
import subprocess
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json


# def getdata(url):
#     r = requests.get(url)
#     return r.text
#
#
# dict_href_links = {}


def get_links(website_link):
    hurl = "https://en.wikipedia.org/wiki/Algorithm"
    req = requests.get(website_link)
    soup = BeautifulSoup(req.text, "html.parser")
    print("The href links are :")
    for link in soup.find_all('a'):
       print(link.get('href'))


# def get_subpage_links(l):
#     for link in tqdm(l):
#         # If not crawled through this page start crawling and get links
#         if l[link] == "Not-checked":
#             dict_links_subpages = get_links(link)
#             # Change the dictionary value of the link to "Checked"
#             l[link] = "Checked"
#         else:
#             # Create an empty dictionary in case every link is checked
#             dict_links_subpages = {}
#         # Add new dictionary to old dictionary
#         l = {**dict_links_subpages, **l}
#     return l


def detect_dns_hijacking(url):
    # Get the IP address for the domain name
    url = url.split('//')
    print(url)
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


# downloadUrl = 'https://ro.wikipedia.org/wiki/Blog'
#
# req = requests.get(downloadUrl)
# filename = req.url[downloadUrl.rfind('/') + 1:]
#
# with open(filename, 'wb') as f:
#     for chunk in req.iter_content(chunk_size=8192):
#         if chunk:
#             f.write(chunk)

# detect_dns_hijacking("example.com")


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
    # dict_links = {website: "Not-checked"}
    # counter, counter2 = None, 0
    # while counter != 0:
    #     counter2 += 1
    #     dict_links2 = get_subpage_links(dict_links)
    #     # Count number of non-values and set counter to 0 if there are no values within the dictionary equal to the string "Not-checked"
    #     counter = sum(value == "Not-checked" for value in dict_links2.values())
    #     # Print some statements
    #     print("")
    #     print("THIS IS LOOP ITERATION NUMBER", counter2)
    #     print("LENGTH OF DICTIONARY WITH LINKS =", len(dict_links2))
    #     print("NUMBER OF 'Not-checked' LINKS = ", counter)
    #     print("")
    #     dict_links = dict_links2
    #     # Save list in json file
    #     a_file = open("data.json", "w")
    #     json.dump(dict_links, a_file)
    #     a_file.close()
    get_links(website)
    detect_dns_hijacking(website)
    #discover_subdirectories(website)


if __name__ == "__main__":
    main()
