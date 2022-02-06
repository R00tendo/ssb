#Count screen looks like: 69/100
import threading
import time
i = 0
def loader(k, a):
 global i
 def go(k,a):
   global i
   i = k
   while i <= a -1: #Run until "i" is bigger than "a"
       time.sleep(0.1)
       print(f"{i}/{a} {' '*10}", end="\r")
 threading.Thread(target=go, args=(k,a,)).start()
def set_value(val):
   global i
   i = val #Sets i's value to the one supplied by the program
