# SSB
![image](https://user-images.githubusercontent.com/72181445/153228795-7346bd04-69eb-4205-9d27-c104ad7295ea.png)
# Current version: Mark_v6

# Description
SSB=simple subdomain bruteforcer

SSB Tries to find subdomains for a domain and scan them for ports/services. When SSB has identified all of the services the subdomain is running, it will then scan the services for common misconfigurations and credentials.

SSB  scans the subdomains for the most common ports and services i've seen in the wild.

# Update log (only major updates)
Update: Mark_v0: Scans for ports in the found subdomains.

Update: Mark_v3: SSH Bruteforce added and ftp threads increased, problems with report generating solved.

Update: Mark_v5: Mysql, Smb, Telnet bruteforce added, rpcbind program lister added, errors now shown in cyan instead of red and SSB can now automatically use sublist3r to scan for subdomains.

# BACKGROUND:
I started this project on 2.2.2022

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


# Features

Mysql Bruteforce<img src="https://user-images.githubusercontent.com/72181445/153476377-b250f42b-b0c0-4153-bc58-e42a9146d960.png" width=200></img>

SSH Bruteforce<img src="https://user-images.githubusercontent.com/72181445/153476527-f709874c-591e-43e7-8bef-bbb0c1d67dfd.png" width=300></img>

FTP Anonymous Account Check<img src="https://user-images.githubusercontent.com/72181445/153476675-e33502cc-53d5-408e-ab80-162c0820343b.png" width=150></img>

FTP Bruteforce

Smb Anonymous Account Check 

Smb Bruteforce

# TECHNICAL DETAILS:

+Uses DNS resolving instead of a port specific or ping scan.


-DNS is slower than using the port scanning method.


+Validates HTTP and HTTPS ports by actually making a request instead of relying off the fact that it is open (many http/https ports that i've seen in the wild are timeouts)


-+Easy to use so that it is fast for pen-testers but also script kiddies can operate this which is bad (Unlike nmap which needs flags to be set right)...

+Automatically scans subdomains without having the need for the hassle of scanning subdomains, making a list, nmap scanning them.

+Does ftp/smb anonyous account checks.

+Reasonable timeouts so you won't have to worry about "Is it even doing anything?/Did it feeze?" because it proceeds to another scan automatically if another one times out.
