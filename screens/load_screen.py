#Loading screen for obvious reasons
import time
import threading
def loader():
 global done
 def go(): 
  global done
  done = False
  a = 0

  while not done:
   time.sleep(0.3)
   a += 1
   if a == 4:
    a = 0
   print(f"Loading{'.' * a + ' ' * (3-a)}", end="\r")

 threading.Thread(target=go).start() #Thread cuz we want to continue to actually do something WHILE it is running

def stop_loading():
    global done
    done = True #Notice "while not done:" line



