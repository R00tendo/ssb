# SSB
![image](https://user-images.githubusercontent.com/72181445/153228795-7346bd04-69eb-4205-9d27-c104ad7295ea.png)
# Current version: Mark_V8

# Put on the night apparence mode so the logos look alot cooler :)

# Description
SSB=simple subdomain bruteforcer

SSB Tries to find subdomains for a domain and scan them for ports/services. When SSB has identified all of the services the subdomain is running, it will then scan the services for common misconfigurations and credentials.

SSB  scans the subdomains for the most common ports and services i've seen in the wild.

# Update log (only major updates)
Update: Mark_v0: Scans for ports in the found subdomains.

Update: Mark_v3: SSH Bruteforce added and ftp threads increased, problems with report generating solved.

Update: Mark_v5: Mysql, Smb, Telnet bruteforce added, rpcbind program lister added, errors now shown in cyan instead of red and SSB can now automatically use sublist3r to scan for subdomains.

Update: Mark_v6: Added HTTP Method detection and PARAMIKO transport.py will get overwritten to prevent error pop ups that would flood the screen if not mitigated (And yes, from my research, updating the actual library is the only way to control the exceptions that are made INSIDE the module)

Update: Mark_v7: Complete redisign of the ui, switching to flag based ui, you can decide wether to only validate or validate AND scan the subdomains

Update: Mark_v8: Added flags and hotfixes

Update: Mark_v9: Added new scan type: light_scan (only service detection)
# Under dev?: Currently yes

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

# Usage:
--help   (not_necessary)    Displays the help page 

-h   (necessary)    Hostname to scan 

--scan-type   (necessary)    Scan types: Validate, light_scan, scan    Validate=validates if subdomain exists light_scan=service detection      scan=all of the mentioned + bruteforce 

-s   (necessary)    Subdomain find method: 1=Sublist3r 2=Wordlist 3=Only this domain 

--dns-threads   (not_necessary)    The amount of threads that will validate subdomains (default=10) 

--web-threads   (not_necessary)    The amount of threads that will be requesting files in the http discovery phase (works only with scan scan_type) (Default:40) 

-w   (not_necessary)    Wordlist (used with -s 2) 

# Examples:
python3 ssb.py -h somerandomassdomain.com -s 1 --scan-type scan 

python3 ssb.py -h somerandomassdomain.com -s 2 -w subdomains.txt --scan-type light_scan

python3 ssb.py -h somerandomassdomain.com -s 1 --scan-type validate

# Features:
<img src="https://user-images.githubusercontent.com/72181445/153476377-b250f42b-b0c0-4153-bc58-e42a9146d960.png" width=200></img>

Mysql Bruteforce


<img src="https://user-images.githubusercontent.com/72181445/153476527-f709874c-591e-43e7-8bef-bbb0c1d67dfd.png" width=300></img>

SSH Bruteforce


<img src="https://user-images.githubusercontent.com/72181445/153476675-e33502cc-53d5-408e-ab80-162c0820343b.png" width=150></img>

FTP Anonymous Account Check

FTP Bruteforce


<img src="https://user-images.githubusercontent.com/72181445/153477452-11306f05-babc-4184-bf40-6ad7050c4f5a.png" width=120></img>

Smb Anonymous Account Check 

Smb Bruteforce


<img src="https://user-images.githubusercontent.com/72181445/153479035-54e630a9-ea77-4a07-b87d-e2af3c9a5e20.png" width=140></img>

Http/Https File Discovery

Http/Https Method Scan


<img src="https://user-images.githubusercontent.com/72181445/153479607-5ba66053-b54b-408c-9ac1-ca7e373cb083.png" width=200></img>

Telnet Bruteforce


<img src="https://user-images.githubusercontent.com/72181445/153480235-d4598870-1175-4b6b-b739-676b9f12f34a.png" width=200></img>

Rpcbind Process Lister


# TECHNICAL DETAILS:

+Uses DNS resolving instead of a port specific or ping scan.


-DNS is slower than using the port scanning method.


+Validates HTTP and HTTPS ports by actually making a request instead of relying off the fact that it is open (many http/https ports that i've seen in the wild are timeouts)


-+Easy to use so that it is fast for pen-testers but also script kiddies can operate this which is bad (Unlike nmap which needs flags to be set right)...

+Automatically scans subdomains without having the need for the hassle of scanning subdomains, making a list, nmap scanning them.

+Does ftp/smb anonyous account checks.

+Reasonable timeouts so you won't have to worry about "Is it even doing anything?/Did it feeze?" because it proceeds to another scan automatically if another one times out.
