import socket
import requests
import warnings
def check(host, port):
   try:
     s = socket.socket()
     s.settimeout(1)
     s.connect((host, int(port)))
     s.close()
     return True
   except:
     return False
def check2(host, port):
   warnings.filterwarnings(action='ignore')
   if port == 80:
     try:
      code = requests.get(f"http://{host}", timeout=4, verify=False).status_code
      code = str(code) + "C"
      return code
     except:
      return "Fals"
   elif port == 443:
     try:
      code = requests.get(f"https://{host}", timeout=4, verify=False).status_code
      code = str(code) + "C"
      return code
     except:
      return "Fals"
   else:
    try:
     s = socket.socket()
     s.settimeout(1)
     s.connect((host, int(port)))
     s.close() 
     return True
    except:
      return "Fals"


