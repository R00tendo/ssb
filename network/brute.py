import threading
from network import host_up
from network import additional
import termcolor
import time
import sys
import os
import socket

#Importing count screen
a = os.getcwd().replace("/network", "")
sys.path.insert(0, a)
from screens import count_screen

def subber(subs, host): 
   global co, trets
   ori = co
   for sub in subs:
      co += 1
      if co ==  ori:
        print("Sleep")
        time.sleep(1)
        ori = co + 400
      count_screen.set_value(co)
      if host == False:
        subcon = f"{sub.strip()}"
      else:
       subcon = f"{sub.strip()}.{host.strip()}"
      try:
         ip = socket.gethostbyname(subcon)
         got.append(subcon)
      except:
         pass
   
   trets -= 1
   sys.exit(0)
  
def dns(subs, host, threads_allowed, scan_type, web_threads):
   global got, co, trets
   got = []
   if subs != False:
    count_screen.loader(0, len(subs))
   co = 0
   ab = 0
   cache = []
   trets = 0

   #Loads subdomain list if it exists (option 3 disables this)
   if subs != False:

    for sub in subs:
      cache.append(sub)
      ab += 1

      if ab == 200:

            #starts threads to subber which dns looks up these domains 
            while trets >= int(threads_allowed):
                  time.sleep(1)
            trets  += 1 
            threading.Thread(target=subber, args=(cache,host,)).start()
            ab = 0
            cache = [] 
    if len(cache) > 0:

        threading.Thread(target=subber, args=(cache,host,)).start()
        ab = 0
        cache = [] 

    while co != len(subs):
        time.sleep(1)

   else:
       got.append(host)
   print(f"Done! {len(got)} subdomains found! {' ' * 10}")
   if scan_type == "validate":
    for host in got:
       print(host)
   else:
    print("\nHost                                |HTTP |HTTPS|SSH |TELNET|FTP |SMTP |RPCBIND|MYSQL|SMB |RDP")
    print("-"*95)

    for subss in got:

        subss = subss.strip()
        #Check if X service is running
        http = host_up.check2(subss, 80) 
        https = host_up.check2(subss, 443)
        ssh = host_up.check2(subss, 22)
        telnet = host_up.check2(subss, 23)
        ftp = host_up.check2(subss, 21)
        smtp = host_up.check2(subss, 25)
        rpcbind = host_up.check2(subss, 110)
        mysql = host_up.check2(subss, 3306)
        smb = host_up.check2(subss, 445)  
        rdp = host_up.check2(subss, 3389)

 
        #Makes open services glow green to make it easier to notice especially when saving the output
        if str(http).lower() != "fals":
             http = termcolor.colored(http, "green")
        if str(https).lower() != "fals":
             https = termcolor.colored(http, "green")
        if str(ssh).lower() != "fals":
             ssh = termcolor.colored(ssh, "green")
        if str(telnet).lower() != "fals":
             telnet = termcolor.colored(telnet, "green")
        if str(ftp).lower() != "fals":
             ftp = termcolor.colored(ftp, "green")
        if str(smtp).lower() != "fals":
             smtp = termcolor.colored(smtp, "green")
        if str(rpcbind).lower() != "fals":
             rpcbind = termcolor.colored(rpcbind, "green")
        if str(mysql).lower() != "fals":
             mysql = termcolor.colored(mysql, "green")
        if str(smb).lower() != "fals":
             smb = termcolor.colored(smb, "green")
        if str(rdp).lower() != "fals":
             rdp = termcolor.colored(rdp, "green")


        print(f"{subss}{' ' * (36 - len(subss))}|{http} |{https} |{ssh}|{telnet}  |{ftp}|{smtp} |{rpcbind}   |{mysql} |{smb}|{rdp}")

        resp = ""
        #This one line is responsible for all the additional scans aka ftp brute, file discovery, etc...
        if scan_type != "light_scan":
         resp = additional.checks(subss, http, https, ssh, telnet, ftp, smtp, rpcbind, mysql, smb, rdp, web_threads)
        
        #If feed_back lenght is over 2 characters print it out. You might be wondering why 2? well the answer to that question is that \n is 2 characters
        if len(resp) > 2:
             print(termcolor.colored(f"RESULTS:{' ' * 10}", "magenta"))
             print(resp)
        print(f"{'-'*36}|{'-'*5}|{'-'*5}|{'-'*4}|{'-'*6}|{'-'*4}|{'-'*5}|{'-'*7}|{'-'*5}|{'-'*4}|{'-'*4}")
    print("Host                                |HTTP |HTTPS|SSH |TELNET|FTP |SMTP |RPCBIND|MYSQL|SMB |RDP")     
