#Parameters checker
import json

def check_special(args):
  if "--help" in args:
     return True
  

def page():
  print("Usage:")
  data = open("json_data/parameters.json").read().strip()
  load_args = json.loads(data)
  for arg in load_args['params']:
    print(f"{arg}   ({load_args['params'][arg]})    {load_args['description'][arg]} ")
  

def nesse(args):
 data = open("json_data/parameters.json").read().strip()
 load_args = json.loads(data)['params']
 for arg in args:
    for necessary_param in load_args:
      if load_args[necessary_param] == "necessary":
       if necessary_param not in args:
           return False
           
 return True

def check(args):
   if args.__len__() < 2:
     return "All of the necessary parameters are not provided..."
   else:
     if not check_special(args):
      if nesse(args):
       return True
      else:
       return "All of the necessary parameters are not provided..."
