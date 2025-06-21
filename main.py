import click
import core.brute
import core.osint
import core.scanner
import utils.logger

title = r"""
  __  ___ ___ ___ __  ___ ___  __  __ __ ___  _   _  __  ___ _  __ 
/' _/| _,\ __| __| _\| __| _ \/  \|  V  | __|| | | |/__\| _ \ |/ / 
`._`.| v_/ _|| _|| v | _|| v / /\ | \_/ | _| | 'V' | \/ | v /   <  
|___/|_| |___|___|__/|_| |_|_\_||_|_| |_|___|!_/ \_!\__/|_|_\_|\_\ 
"""

def show_title():
    click.echo(title)

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


def menu(mode, type, input, userlist, passlist, verbose):
    show_title()

    if mode == "brute":
        if not type or not input or not userlist or not passlist:
            click.echo("❌  Para fuerza bruta debes indicar --type, --input, --userlist y --passlist.")
            return
        click.echo(f"🔍 Running brute force in {input} (tipo: {type})...")
        core.brute.run(type, input, userlist, passlist, verbose)

    elif mode == "osint":
        if not type or not input:
            click.echo("❌  OSINT requires --type y --input.")
            return
        click.echo(f"🕵️ Running osint about {input} (tipo: {type})...")
        core.osint.run(type, input, verbose)

    elif mode == "scanner":
        if not type or not input:
            click.echo("❌  Scanner requires --type y --input.")
            return
        click.echo(f"🔎 Scanning {input} (tipo: {type})...")
        core.scanner.run(type, input, verbose)

    elif mode == "logger":
        if not type or not input:
            click.echo("❌  Logger requieres --type y --input.")
            return
        click.echo(f"📝 Running logger in {input} (tipo: {type})...")
        utils.logger.run(type, input, verbose)

    else:
        click.echo("❌  Invalid mode.")

if __name__ == "__main__":
    menu()
