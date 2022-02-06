from termcolor import colored
from screens import count_screen
from ftplib import FTP
import threading
import os
import time
import requests
import random

#FTP SECTION!


#FTP Thread
def ftp_brute(combos, host):
   global bt, feed_back, trets
   wordlist = combos
   for combo in wordlist:
                     #Beutifies the combo by splitting it with :
                     count_screen.set_value(bt)
                     combo = combo.strip()
                     combo = combo.split(":")

                     try:
                        ftp = FTP(host, timeout=3)
                        ftp.login(user=combo[0], passwd=combo[1], acct='')
                        ftp.quit()
                        feed_back = feed_back + colored(f"\n [CREDENTIALS] FTP CREDENTIALS CRACKED: username:{combo[0]} password:{combo[1]}", "red")
                            
                     except: 
                         pass 
   trets -= 1
def ftp_check(host):
       global bt, trets, feed_back
       feed_back = ""

       #FTP Anonymous login test
       try:
         ftp = FTP(host)
         ftp.login()
         ftp.quit()
         feed_back = feed_back + colored(" [VULNERABILITY] FTP ANONYMOUS LOGIN IS ENABLED!", "red")
       except:
         pass

       if len(feed_back) >= 0:
              #Initial variables
              print(colored("[INFO] Starting FTP Bruteforce attack...", "green"))
              wordlist = open("wordlists/ftp-combo.txt").readlines()
              bt = 0
              trets = 0
              cache = []
              count_screen.loader(bt, len(wordlist))

              #Reads trough wordlist and starts threads
              for line in wordlist:
                     while trets > 5:
                           time.sleep(0.2)
                     line=line.strip()
                     threading.Thread(target=ftp_brute, args=([line], host)).start()
                     trets += 1
                     bt += 1

              bt += 1  #Array starts at 0 so we have to add one to make it stop

              #Finishing off
              count_screen.set_value(bt)
              time.sleep(0.5)
              print(colored("[INFO] FTP bruteforce complete", "green"))
        
       return feed_back
#FTP BRUTE ENDS








#HTTP/HTTPS File discovery starts here




#Tries to identify the signs of a bad response
def http_wrong_calc(url):
    #You know them, you love them, variables!
    sample_codes = []
    sample_lenghts = []
    which_one = 0
    bad_status = ""
    bad_len = ""


    #Gets an example of the front page (we assume that the main site isn't 404 or 403)
    good = requests.get(url)

    #You can increase the samples if you suspect that the site isn't responding correctly all the time
    for i in range(1):


       #Create a made up url address that 99.99999999999999999% doesn't exist
       urla = url + "/" + str(random.randint(1,9999999))

       head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
       }
        

      
       a = requests.get(urla, headers=head)
       #Compares status code and lenght.
       if a.status_code != good.status_code:
              print(colored("[INFO] Bad status code found:" + str(a.status_code), "green"))
              bad_status = a.status_code
              which_one = 1
       elif a.status_code == good.status_code and len(a.text) != len(good.text):
              print(colored("[INFO] Bad lenght found: " + str(len(a.text), "green")))
              bad_len = len(a.text)
              which_one = 2
       else:
           print(colored("[ERROR] Can't find anything that differes in good and bad requests...", "red"))
   

    #Returns the results to http_check
    if which_one == 1:
       return which_one, bad_status
    elif which_one == 2:
       return which_one, bad_len
    else:
        print(colored(f"[ERROR] not a bad or good len {which_one}", "red"))


def http_brute_thread(lis, bad, bad_what, url):
    global trets, bt, allowed
    allo = 0
    lsy = 0
    #Checks what mode to detect bad response, the options are from the lenght and from the status_code
    if bad_what == 1:
        bad_status = bad
    elif bad_what == 2:
        bad_len = bad

    #Goes trough the X amount of files in the mini list created by http_brute
    for line in lis:
       #1 second sleep after 8 requests, this helps to not overload requests and no, this is way better than lowering threads since it's not the internet connection but over usage of a library
       lsy += 1
       if lsy > 8:
         time.sleep(1)
         lsy = 0


       bt += 1
       count_screen.set_value(bt)
       line = line.strip()
       requ = False

       #User-Agent to make it look like we're not a bot
       head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
       }
       try:
        requ = requests.get(url + "/" + line, headers=head)
       except:
         #If timeout 20 times, set running threads manually to 0 and increase bt to trillion in order to stop the count screen and then exit
         allo += 1
         time.sleep(3)
         if allo > 20:
             bt = 1000*1000*1000
             trets = 0 
             exit()
        #this one below this comment was a prototype but the problem is that it 1. went to -   2. because there are a lot of threads it would remove all of them instant if even a second delay
#        allo = allowed -1
#        print(colored(f"[ERROR] Connection error... Reducing threads from {allowed} to {allo}", "red"))
#        allowed = allo
      

  
       #Adds found files to a list that would be turned to a report further down the line
       if requ != False:
        if bad_what == 1:
          if requ.status_code != int(bad_status):
                http_found.append(f"{line} Code:{requ.status_code}")
        if bad_what == 2:
          if len(requ) != int(bad_len):
                http_found.append(f"{line} Len:{len(requ.text)}")
   
    trets -= 1
     
   
    return http_found

#Http thread launcher, you can modify the amount of threads running from the allowed variable
def http_brute(url, wordlist, bad, bad_what):
     global http_found, trets, bt, allowed
     print(url)
     http_found = []
     #Checks if wordlist exists
     if not os.path.exists(wordlist):
          print(colored("[NOT FOUND] HTTP brute wordlist not found", "red"))
          sys.exit(1)
     
     #Loads wordlist and sets up the initial variables
     cache = []
     trets = 0
     lines = open(wordlist, "r").readlines()
     bt = 0
     count_screen.loader(0, len(lines))
     allowed = 40 #<--  Threads

     #Starts threads
     for line in lines:
         line = line.strip()
         cache.append(line)         
         if trets < allowed:
             if len(cache) > 9:
                 trets += 1
                 threading.Thread(target=http_brute_thread, args=(cache, bad, bad_what, url,)).start()
                 cache = []
         while trets >= allowed:
                time.sleep(0.4)
     if len(cache) != 0:
         threading.Thread(target=http_brute_thread, args=(cache, bad, bad_what, url,)).start()
         cache = []
      
     while trets > 0 or bt != len(lines):
         time.sleep(1)
         if len(cache) != 0:
           threading.Thread(target=http_brute_thread, args=(cache, bad, bad_what, url,)).start()
           cache = []
 
     #Generates a report
     if len(http_found) < len(lines):

      http_fdback = ""
      for found in http_found:
            http_fdback = http_fdback + colored(f" [{url.split(':')[0].upper().strip()}_CONTENT] {found.strip()}\n", "yellow")
     return http_fdback

#The first step, aka determining what to run and loads wordlists
def http_check(host, p_s):
   http_feed_back = ""
   if p_s == "http":
      prefix = "http://"
   elif p_s == "https":
      prefix = "https://"
   else:
     print(colored(f"[ERROR] {p_s} is not http nor is it https", "red"))
   host = host.strip()
   url = prefix + host
   try:
    whi, bad = http_wrong_calc(url)
   except:
    return colored(" [Error] in running file discovery, server not responding...", "red")
   wordlist = "wordlists/http-disco.txt"

   http_feed_back = http_brute(url, wordlist, bad, whi)
   return http_feed_back

#HTTP/HTTPS File discovery stops here






#Central hub to decide what scans to run
def checks(host, http, https, ssh, telnet, ftp, smtp, rpcbind, mysql, smb, rdp):
     only_https = False
     feed_back = ""
     #FTP scan start if ftp != Fals
     if ftp != "Fals":
       ftp_check_res = ftp_check(host)
       feed_back = feed_back + ftp_check_res









     #HTTP/HTTPS scan or even both if one is open
     if http != "Fals" or https != "Fals":
        if http != "Fals" and https != "Fals":


           #Ran into a problem that is that most sites have http and https ports open but when you goto http, it will redirect you to the https version, this helps to mitigate lost time
           try:
             requests.get(f"http://{host}", allow_redirects=False).headers['Location']
             only_https = True
           except:
                pass
           if only_https: 
               print(colored("[INFO] Http to https redirect found, ignoring http port and continuing to scan https...", "green"))
               http_s_results = http_check(host, "https")
               feed_back = feed_back + http_s_results





           else:
            #If not a redirect
            p_s = ['http', 'https']
           
            for proto in p_s:
             print(colored(f"[INFO] Scanning {proto}", "green"))
             http_s_results = http_check(host, proto)
             feed_back = feed_back + http_s_results
             

        #Only one running (http/https)
        elif  http != "Fals" or https != "Fals":  

           if http != "Fals":
               p_s = "http"
               http_s_results = http_check(host, p_s)
               feed_back = feed_back + http_s_results
               
           elif https != "Fals":
               p_s = "https"
               http_s_results = http_check(host, p_s)
               feed_back = feed_back + http_s_results
               
           else:
              print(colored("[ERROR] neither http or https", "red"))
              sys.exit(1)

           


          
     return feed_back
     exit()
