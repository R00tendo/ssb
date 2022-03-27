#!/usr/bin/python3
from screens import  load_screen
from screens import  count_screen
from network import  host_up
from files   import  reader
from network import  brute #<-- does the actual brute forcing
from others import help 
from others import param
import threading
import os
import termcolor
import time
import sys
import socket
import paramiko



#It overwrites the paramiko transport.py file with the same one but with the errors removed so that the script works better
dest = paramiko.__file__.replace("__init__.py", "") + "transport.py"
src = "modules/paramiko/transport.py"
if os.path.exists(src):
 if os.path.exists(dest):
   if open(src).read() != open(dest).read():
          print(f"{dest} Was overwritten with a custom one that doesn't spam your screen with errors!")
          src_read = open(src, 'rb').read()
          dest_write = open(dest, 'wb').write(src_read)
#          os.system("cp  modules/paramiko/transport.py " + dest)


#Cool logo
banner = termcolor.colored("""
                                                                                                    
                                                         ^???7.                                     
                                                        :YYYY^                                      
                                                        ?YJY~                                       
                                                       !YJY?.                                       
                                                      ~YJYJ:                                        
                     :!7777777777^   .~7777777777!   :JYJY7^!!!777:                                 
                    ^YYYYYYYJYYYY~  .JYYYYYYJYYYY?  .7YJJYYYYYYYYY~                                 
                   :YJJJ:...7YYY7   ?YJY~ ..^YYYJ.  ~YJYJ~^::?YJY!                                  
                   JYJYJ!:  :^^^.  !YJJJ7^. .^^^:  :YJJY:   !YJY?.                                  
                   ~?JYYYY?!:      ^7JYYYYJ7~.    .JYJY~   ^YYJJ:                                   
                     .~7JJYYYJ.      .^!JJJYYY~   7YJY7   :JYJY~                                    
                :7777.  .7YJY?.  ~777^   ~JJYJ^  ~YJYJ.   7YJY?                                     
               .?YYY?^^^^JJYJ:  ~YYYY~^^:7YJY!  :JJJY!:^^7YJYJ.                                     
               !YYYYYYYYYYYJ^  .YYYYYYYYYYYY7  .JYYYYYYYYYYYJ:                                      
               :~!!!!!!!!!^.    ~!!!!!!!!!~^   ^!!!!!!!!!~~:.                                       
                           @R00tendo at github                                                      
                                                                                                    
                                                                                           
""", 'green')

print(banner.strip())
if "bool" not in str(type(help.check(sys.argv))):
   help.page()
   sys.exit(0)

#Parameter section
parameters = param.get_params(sys.argv)

if parameters.error:
   print(parameters.error)
   sys.exit(1)


if parameters.help:
  help.page

try:
  dns_threads = parameters.dns_threads
except: 
  print("Invalid dns_threads! Please look at the help page (--help) to see how to use this tool.")
  sys.exit(1)


try:
  int(parameters.method)
except: 
  print("Invalid Subdomain finding method! Please look at the help page (--help) to see how to use this tool.")
  sys.exit(1)

try:
  int(parameters.web_threads)
except: 
  print("Invalid Web_Threads! Please look at the help page (--help) to see how to use this tool.")
  sys.exit(1)
web_threads=parameters.web_threads

scan_type = parameters.scan_type.lower()
if scan_type != "validate" and scan_type != "scan" and scan_type != "light_scan":
   print("Invalid scan_type! Please look at the help page (--help) to see how to use this tool.")
   sys.exit(1)



#Host dead?
host = parameters.hostname
try:
  socket.gethostbyname(host)
except:
  print(f"Cannot resolve {host} to an ip...")
  sys.exit(1)


print("Host is up or ip supplied!\n")

wordlist = parameters.wordlist
word_or_sub = parameters.method

#Sublist3r method
if word_or_sub == "1":
    if len(os.popen("sublist3r").read()) != 0:


     load_screen.loader()
     os.system(f"sublist3r -d {host} -o subs-{host}-ssb >/dev/null ")
     load_screen.stop_loading()

     time.sleep(1)
     print(f"Done! {' '*10}")

     if not os.path.exists(f"subs-{host}-ssb"):
         print("Sublist3r couldn't find any subdomains... Maybe try the wordlist one? Sometimes sites block web crawlers from indexing the site at all.")
         sys.exit(1)

     #Cache file read, write
     parse_out = open(f"subs-{host}-ssb", "r").readlines()
     open(f"subs-{host}-ssb", "w").write("")

     write_new = open(f"subs-{host}-ssb", "a")
     for line in parse_out:
       if "." in line:
           write_new.write(line.split(f".{host}")[0] + "\n")
     write_new.close()

     print(f"Sublist3r found {len(parse_out)} subdomains!")
    else:
      print("Couldn't find sublist3r, please install it from: https://github.com/aboul3la/Sublist3r")
elif word_or_sub == "2":
    pass
elif word_or_sub == "3":
    pass
else:
    print("Invalid option, options are 1,2,3")
    sys.exit(1) 



#Determines what to ask
if word_or_sub == "2":
 pass

elif word_or_sub == "1":
  wordlist = f"subs-{host}-ssb"

if word_or_sub != "3":
 if not os.path.exists(wordlist):
    print(f"Cant find {wordlist} or wordlist not specified, if so please do so by using -w")
    sys.exit(1)

if word_or_sub != "3":
 allowed = str(dns_threads)

else:
  allowed = "1"




if word_or_sub == "2":
 print("\nLoading wordlist into memory...")
elif word_or_sub == "1":
   print("Going trough the subdomains...")


#Loading screen
load_screen.loader()
time.sleep(0.4)

if word_or_sub != "3":
  subs = reader.read(f"{wordlist}")
else:
   subs = False


load_screen.stop_loading()
time.sleep(0.5)




if word_or_sub != "3":
 print(f"Done, {len(subs)} words loaded! {' ' * 10}")

time.sleep(1)


#Removes sublist3r cache if it exists
if word_or_sub == "1":
    print(f"Removing cache file: subs-{host}-ssb")
    try:
      os.remove(f"subs-{host}-ssb")
    except:
      print("Removal fail... Continuing without removing it.")


#Our journey begins!
print("\nStarting DNS Bruteforce...")
brute.dns(subs, host, allowed, scan_type, web_threads)

