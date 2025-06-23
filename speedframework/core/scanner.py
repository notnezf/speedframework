
from utils.common import loadListOrValue
from utils.print import warning,info,success,error

## Functions

def scanPortsBasic():
    warning("🌐 Basic scan form module not yet implemented.")
def scanPortsNmap():
    warning("🌐 Nmap Scan form module not yet implemented.")
def detectServices():
    warning("🌐 Detect services module not yet implemented.")
def detectWebTech():
    warning("🌐 Detect web technologies module not yet implemented.")

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