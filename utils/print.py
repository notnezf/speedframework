import click
from termcolor import colored

def info(msg): click.echo(colored(msg, 'cyan'))
def success(msg): click.echo(colored(msg, 'green'))
def warning(msg): click.echo(colored(msg, 'yellow'))
def error(msg): click.echo(colored(msg, 'red'))

ascii_title = r"""
  __  ___ ___ ___ __  ___ ___  __  __ __ ___  _   _  __  ___ _  __ 
/' _/| _,\ __| __| _\| __| _ \/  \|  V  | __|| | | |/__\| _ \ |/ / 
`._`.| v_/ _|| _|| v | _|| v / /\ | \_/ | _| | 'V' | \/ | v /   <  
|___/|_| |___|___|__/|_| |_|_\_||_| |_|___|!_/ \_!\__/|_|_\_|\_\ 
"""

def show_title():
    click.echo(colored(ascii_title, 'blue'))
