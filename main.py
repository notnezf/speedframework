import argparse
import core.brute
import core.osint
import core.scanner

title = r"""
  __  ___ ___ ___ __  ___ ___  __  __ __ ___  _   _  __  ___ _  __ 
/' _/| _,\ __| __| _\| __| _ \/  \|  V  | __|| | | |/__\| _ \ |/ / 
`._`.| v_/ _|| _|| v | _|| v / /\ | \_/ | _| | 'V' | \/ | v /   <  
|___/|_| |___|___|__/|_| |_|_\_||_|_| |_|___|!_/ \_!\__/|_|_\_|\_\ 
"""

options = """
Select one of these options:
-b brute force attacks
-o osint
-s scan target
"""

def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", choices=['brute','scanner','osint'], required=True, help="Mode of operation")
    parser.add_argument("-t", "--type", help="Specific type of attack/scan")
    parser.add_argument("-i", "--input", help="Target input (IP/domain)")
    parser.add_argument("-u", "--userlist", help="Username list")
    parser.add_argument("-p", "--passlist", help="Password list")
    args = parser.parse_args()
    print(title)
    if args.mode == "brute":
        print("Running bruteforce...")
    elif args.mode == "osint":
        print("Running OSINT...")
    elif args.mode == "scanner":
        print("Running scanner...")
    else:
        print("Invalid mode.")
menu()