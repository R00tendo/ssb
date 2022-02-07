# ssb
![image](https://user-images.githubusercontent.com/72181445/152828512-214ecf43-37eb-4013-87d3-2eff6fffc354.png)
# Current version: Markv5

# Description
SSB=simple subdomain bruteforcer
SSB is a tool that bruteforces subdomains based on dns records.
SSB also scans the subdomains for the most common ports i've seen in the wild.


# Update log (only major updates)
Update: markv3: SSH Bruteforce added and ftp threads increased, problems with report generating solved

Update: markv5: Mysql, Smb, Telnet bruteforce added, rpcbind program lister added, errors now shown in cyan instead of red

# HOW TO SETUP:

pip3 install requests

pip3 install termcolor

pip3 install ftplib

pip3 install paramiko

sudo apt-get install libmariadb3 libmariadb-dev

pip3 install mariadb

pip3 install smbprotocol

pip3 install telnetlib

And you're done, now just launch the app using PYTHON3

python3 ssb.py




# TECHNICAL DETAILS:

+Uses DNS resolving instead of a port specific or ping scan.


-DNS is slower than using the port scanning method.


+Validates HTTP and HTTPS ports by actually making a request instead of relying off the fact that it is open (many http/https ports that i've seen in the wild are timeouts)


-+Easy to use so that it is fast for pen-testers but also script kiddies can operate this which is bad (Unlike nmap which needs flags to be set right)...

+Automatically scans subdomains without having the need for the hassle of scanning subdomains, making a list, nmap scanning them.

+Does ftp/smb anonyous account checks.

+Reasonable timeouts so you won't have to worry about "Is it even doing anything?/Did it feeze?" because it proceeds to another scan automatically if another one times out.
