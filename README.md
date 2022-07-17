# SSB
![image](https://user-images.githubusercontent.com/72181445/153228795-7346bd04-69eb-4205-9d27-c104ad7295ea.png)
# Current version: Mark_V13.3.2

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

Update: Mark_v10: Flag ui upgraded to argparse 

Update: Mark_v11: ssb now uses 3 different programs to find subdomains (sublis3r,findomain,assetfinder)

Update: Mark_v11.2.1: Added url discovery and finding sensitive files in those urls, fixed bug in color handling

Update: Mark_v13.3.2: Added target list mode, colored errors, fixed alot of stuff :D
# Under dev?: Only bug fixes

# BACKGROUND:
I started this project on 2.2.2022

# HOW TO SETUP:

chmod +x install.sh

./install.sh

And you're done, now just launch the app using PYTHON3

python3 ssb

# Usage:  
  -h, --help            show this help message and exit
  
  -t [TARGET], --target [TARGET]
                        (not_necessary) Target to scan
                        
  -tl [TARGET_LIST], --target-list [TARGET_LIST]
                        (not_necessary) Target list (used with -s 4)
                        
  --scan-type SCAN_TYPE, --scan-type SCAN_TYPE
                        (necessary) Scan types: Validate, light_scan,
                        scan Validate=validates if subdomain exists
                        light_scan=service detection scan=all of the mentioned
                        + bruteforce
                        
  -s SCAN_METHOD, --scan-method SCAN_METHOD
                        (necessary) Subdomain find method:
                        1=Automated 2=Wordlist 3=Only this domain 4=Read
                        targets from a list (no subdomain enumeration)
                        
  --dns-threads [DNS_THREADS], --dns-threads [DNS_THREADS]
                        (not_necessary) The amount of threads that will
                        validate subdomains (default=10)
                        
  --web-threads [WEB_THREADS], --web-threads [WEB_THREADS]
                        (not_necessary) The amount of threads that will be
                        requesting files in the http discovery phase (works
                        only with scan scan_type) (Default:40)
                        
  -w [WORDLIST], --wordlist [WORDLIST]
                        (not_necessary) Wordlist (used with -s 2)

# Examples:
python3 ssb.py -t somerandomassdomain.com -s 1 --scan-type scan 

python3 ssb.py -t somerandomassdomain.com -s 2 -w subdomains.txt --scan-type light_scan

python3 ssb.py -t somerandomassdomain.com -s 1 --scan-type validate

python3 ssb.py -tl hosts.txt -s 4 --scan-type scan
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

Url discovery, sensitive file discovery

<img src="https://user-images.githubusercontent.com/72181445/153479607-5ba66053-b54b-408c-9ac1-ca7e373cb083.png" width=200></img>

Telnet Bruteforce


<img src="https://user-images.githubusercontent.com/72181445/153480235-d4598870-1175-4b6b-b739-676b9f12f34a.png" width=200></img>

Rpcbind Process Lister




# TECHNICAL DETAILS:

+Uses DNS resolving instead of a port specific or ping scan.


-DNS is slower than using the port scanning method.


+Validates HTTP and HTTPS ports by actually making a request instead of relying off the fact that it is open (many http/https ports that i've seen in the wild are timeouts)


-+Easy to use so that it is fast for pen-testers but also script kiddies can operate this which is bad...

+Automatically scans subdomains without having the need for the hassle of scanning subdomains, making a list, nmap scanning them.

+Does ftp/smb anonyous account checks.

+Reasonable timeouts so you won't have to worry about "Is it even doing anything?/Did it feeze?" because it proceeds to another scan automatically if another one times out.
