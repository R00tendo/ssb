import json
def setter(arg1, arg2):
# global parameters
 arg2 = str(arg2)
 if arg2.__len__() < 1: return
 if arg1 == "--help":
     parameters.help = True
 elif arg1 == "-h":
     parameters.hostname = arg2
 elif arg1 == "--scan-type":
     parameters.scan_type = arg2
 elif arg1 == "-s":
     parameters.method = arg2
 elif arg1 == "--dns-threads":
     parameters.dns_threads = arg2
 elif arg1 == "--web-threads":
     parameters.web_threads = arg2
 elif arg1 == "-w":
     parameters.wordlist = arg2  
 else:
     parameters.error = f"Invalid option {arg1}"

def get_params(args):
 global parameters
 class parameters:
     hostname = ""
     scan_type = ""
     method = ""
     help = False
     dns_threads = 10
     web_threads = 40
     wordlist = ""
     error = ""
# parameters = []
 data = open("json_data/parameters.json").read().strip()
 load_args = json.loads(data)['params']
 for arg in args:
    if arg in load_args:
      if args.index(arg) +1 != len(args):
         if args[args.index(arg) + 1] in load_args:
             return False
         else:
             setter(arg, args[args.index(arg) + 1])
      else:
          return False
 return parameters
