#!/usr/bin/env python

# Shell Algorithm  ||
#                  ||
#                  ||
#                  \/

# 1.    Create prompt
# 2.    Get command
# 3.    Validate command
# 4.    Execute

# Importing function essential for shell

import sys
import os 
import __builtin__
import imp

# Red coloring

r = "\033[31m"

# White coloring

w = "\033[0"

# Green coloring

g = "\033[32"

# Blue coloring

b = "\033[34"

# This clears the shell

os.system("clear")

# Sets up a custom interactive python shell

sys.ps1 = g + "[pycmd]$ " + w

# Pycmd set up

# Module loading function
# {

def importmodule(module):
  
  try:
    
    
    modulename = "modules/" + module + ".py"
    ModuleFile = open(modulename, "rb")
    mod =imp.loadsource(module, modulename, ModuleFile)
    
    # }
    
    # Updating loaded module list
    
    _builtin__.__dict__.update(mod.__dict__)
    print w + "Module " + module + " loaded..."
    
    # Adding [modulename] to console to see which module
    # is currently loaded
    
    sys.ps1 = g + "[pycmd]$ " + b + "<" + module + ">" + w
    
    # Closing ModuleFile
    
    Finally:
      
      try: Module.close()
        
        execept: pass

def loadmodule(mname):
  _importmodule(mname)


os.environ["PYTHONINSPECT"] = True
