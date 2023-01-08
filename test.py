import requests
import socket
import subprocess
import os


def detect_dns_hijacking(url):
    # Get the IP address for the domain name
    url=url.split('//')
    #print(url)
    try:
        ip_address = socket.gethostbyname(url[1])
        print(ip_address)
    except socket.gaierror:
        print("Error: Could not resolve domain name.")
        return
    dns_server = socket.gethostbyname(url[1])  # Get the DNS server for the domain name
    #print(dns_server)
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
    str="gobuster -e -u "+url+" -w /usr/share/wordlists/common.txt"
    print(str)
    os.system(str)
    #subdirectories = subprocess.run(["gobuster", "-e ", "-u ", "https://mta.ro/", "-w ", "/usr/share/wordlists/common.txt"],capture_output=True).stdout

    # Print the subdirectories
    #print("Subdirectories:")
    #print(subdirectories.decode())





# deci teoretic un actor care intra pe aplicatie ar insera un link sa zicem si s-ar descarca acest fisier
# acum urmatorul pas ar fi aplicarea metodei 2-gram peste acest fisier

def main():
    url = input("Enter website:")
    detect_dns_hijacking(url)
    discover_subdirectories(url)

if __name__ == "__main__":
    main()
