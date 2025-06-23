
from utils.common import loadListOrValue
from utils.print import warning,info,success,error

## Functions

def scanPortsBasic():
    warning("🌐 HTTP form module not yet implemented.")
def scanPortsNmap():
    warning("🌐 HTTP form module not yet implemented.")
def detectServices():
    warning("🌐 HTTP form module not yet implemented.")
def detectWebTech():
    warning("🌐 HTTP form module not yet implemented.")

## Run module

def run(type,input,verbose):
    if type == "basic":
        scanPortsBasic()
    elif type == "nmap":
        scanPortsNmap()
    elif type == "servicedetect":
        detectServices()
    elif type=="webtech":
        detectWebTech()
    else:
        print("mode not selected")