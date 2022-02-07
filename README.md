# ssb
![image](https://user-images.githubusercontent.com/72181445/152828512-214ecf43-37eb-4013-87d3-2eff6fffc354.png)


SSB=simple subdomain bruteforcer
SSB is a tool that bruteforces subdomains based on dns records.
SSB also scans the subdomains for the most common ports i've seen in the wild.

Update: markv3: SSH Bruteforce added and ftp threads increased, problems with report generating solved

Update: markv5: Mysql, Smb, Telnet bruteforce added, rpcbind program lister added, errors now shown in cyan instead of red

# HOW TO USE:

pip3 install requests

pip3 install termcolor

pip3 install ftplib

pip3 install paramiko

sudo apt-get install libmariadb3 libmariadb-dev

pip3 install mariadb

pip3 install smbprotocol

pip3 install telnetlib

python3 ssb.py




# TECHNICAL DETAILS:

+Uses DNS resolving instead of scanning a specific port.


-DNS is slower than using the port scanning method.


+Validates HTTP and HTTPS ports by actually making a request instead of relying off the fact that is open (many http ports that i've seen in the wild are timeouts)


-+easy to use so it's fast for pen testers but also script kiddies can operate this which is bad...


+No need to make a list and after that nmap them aka it covers a lot more of attack surface with in a short time
