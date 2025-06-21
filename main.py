import click
import core.brute
import core.osint
import core.scanner
import utils.logger

from utils.print import info, success, warning, error, show_title


@click.command(help="""
Modular pentesting tool.

Available modes:
  - brute   → Brute-force attacks (requires: -t, -i, -u, -p)
  - osint   → Open Source Intelligence gathering (requires: -t, -i)
  - scanner → Target scanning (requires: -t, -i)
  - logger  → Event or activity logging (requires: -t, -i)

Optional:
  --port    → Set a custom port (default varies per module)

Example:
  python main.py -m brute -t ssh -i target.com -u users.txt -p passwords.txt --port 2220 --verbose
""")
@click.option("-m", "--mode", required=True,
              type=click.Choice(['brute', 'scanner', 'osint', 'logger']),
              help="Operation mode")
@click.option("-t", "--type", help="Specific attack or scan type")
@click.option("-i", "--input", help="Target IP address or domain")
@click.option("-u", "--userlist",
              type=click.Path(exists=True, readable=True, dir_okay=False),
              help="Path to user list file")
@click.option("-p", "--passlist",
              type=click.Path(exists=True, readable=True, dir_okay=False),
              help="Path to password list file")
@click.option("--port", type=int, help="Custom port to use")
@click.option("--verbose", is_flag=True, help="Enable verbose output")
def menu(mode, type, input, userlist, passlist, port, verbose):
    show_title()

    if mode == "brute":
        if not all([type, input, userlist, passlist]):
            error("❌ Brute-force mode requires --type, --input, --userlist, and --passlist.")
            return

        if port is None:
            port = 22 if type == "ssh" else 21 if type == "ftp" else 80

        info(f"🔍 Running brute force on {input}:{port} (type: {type})...")
        core.brute.run(type, input, userlist, passlist, port, verbose)

    elif mode == "osint":
        if not type or not input:
            error("❌ OSINT mode requires --type and --input.")
            return
        info(f"🕵️ Running OSINT on {input} (type: {type})...")
        core.osint.run(type, input, verbose)

    elif mode == "scanner":
        if not type or not input:
            error("❌ Scanner mode requires --type and --input.")
            return
        info(f"🔎 Scanning {input} (type: {type})...")
        core.scanner.run(type, input, verbose)

    elif mode == "logger":
        if not type or not input:
            error("❌ Logger mode requires --type and --input.")
            return
        info(f"📝 Running logger on {input} (type: {type})...")
        utils.logger.run(type, input, verbose)

    else:
        error("❌ Invalid mode.")

if __name__ == "__main__":
    menu()
