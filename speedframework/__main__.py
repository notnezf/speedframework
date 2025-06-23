## Necessary libraries
import click

## Custom modules
import core.brute
import core.osint
import core.scanner
import utils.logger
from utils.print import info, success, warning, error, show_title

## CLI definition
@click.command(help="""
Modular pentesting tool.

Modes:
  brute   → brute-force (needs -t -i -u -p)
  osint   → information gathering (needs -t -i)
  scanner → port / service scan (needs -t -i)
  logger  → event logging (needs -t -i)

Optional:
  --port  → custom port (default depends on module)

Example:
  python main.py -m brute -t ssh -i target.com -u users.txt -p passwords.txt --port 2220 --verbose
""")


@click.option("-m", "--mode", required=True,
              type=click.Choice(['brute', 'scanner', 'osint', 'logger']),
              help="Select working mode")
@click.option("-t", "--type",  help="Attack / scan subtype")
@click.option("-i", "--input", help="Target IP or domain")
@click.option("-u", "--userlist", help="User list file or single username")
@click.option("-p", "--passlist", help="Password list file or single password")
@click.option("--port", type=int, help="Custom port number")
@click.option("--verbose", is_flag=True, help="Show failures too")


def menu(mode, type, input, userlist, passlist, port, verbose):
    ## Show ASCII banner
    show_title()

    ## Brute-force block
    if mode == "brute":
        if not all([type, input, userlist, passlist]):
            error("❌ Need --type, --input, --userlist, --passlist.")
            return

        ## Auto-port if user did not set one
        if port is None:
            port = 22 if type == "ssh" else 21 if type == "ftp" else 80

        info(f"🔍 Brute-forcing {input}:{port} ({type})")
        core.brute.run(type, input, userlist, passlist, port, verbose)

    ## OSINT block
    elif mode == "osint":
        if not type or not input:
            error("❌ Need --type and --input for OSINT.")
            return
        info(f"🕵️ OSINT on {input} ({type})")
        core.osint.run(type, input, verbose)

    ## Scanner block
    elif mode == "scanner":
        if not type or not input:
            error("❌ Need --type and --input for scanner.")
            return
        info(f"🔎 Scanning {input} ({type})")
        core.scanner.run(type, input, verbose)

    ## Logger block
    elif mode == "logger":
        if not type or not input:
            error("❌ Need --type and --input for logger.")
            return
        info(f"📝 Logging on {input} ({type})")
        utils.logger.run(type, input, verbose)

    ## Fallback if mode typo
    else:
        error("❌ Invalid mode.")

## Entrypoint
if __name__ == "__main__":
    menu()
