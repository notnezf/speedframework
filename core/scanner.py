def scanPortsBasic():
    pass
def scanPortsNmap():
    pass
def detectServices():
    pass
def detectWebTech():
    pass
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