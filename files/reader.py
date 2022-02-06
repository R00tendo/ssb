#Reads a wordlist
def read(file):
   subs = []
   with open(file, "r", encoding="latin-1") as lines:
       for line in lines:
              line = line.strip()
              subs.append(line)
   return subs
