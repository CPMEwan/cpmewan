#!/usr/bin/python

import random
from time import sleep
import signal, sys, os
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.color import Color
from rich.text import Text
import numpy as np
from datetime import datetime
import pytz

utcmoment_naive = datetime.utcnow()
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

# print "utcmoment_naive: {0}".format(utcmoment_naive) # python 2
print("utcmoment_naive: {0}".format(utcmoment_naive))
print("utcmoment:       {0}".format(utcmoment))

localFormat = "%Y-%m-%d %H:%M:%S"

timezones = ['America/Los_Angeles', 'Europe/Madrid', 'America/Puerto_Rico']

for tz in timezones:
    localDatetime = utcmoment.astimezone(pytz.timezone(tz))
    print(localDatetime.strftime(localFormat))

# utcmoment_naive: 2017-05-11 17:43:30.802644
# utcmoment:       2017-05-11 17:43:30.802644+00:00
# 2017-05-11 10:43:30
# 2017-05-11 19:43:30
# 2017-05-11 13:43:30

from cpmewan import CPMEwan

__CHANNEL_USERNAME__ = "Ewan1999Ewan"
__GROUP_USERNAME__ = "Ewan19_99Ewan"


def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = """ ▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ 
▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ 
▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒
▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░
░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
  ░  ▒   ░▒ ░     ░  ░      ░ ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░░ ░░   ░ ▒░
░        ░░       ░      ░      ░     ░   ░    ░   ▒      ░   ░ ░ 
░ ░                      ░      ░  ░    ░          ░  ░         ░ 
░                                                                 """
    start_color = Color.parse("#28e99a")
    end_color = Color.parse("#cbd31a")
    start_rgb = np.array(start_color.triplet)
    end_rgb = np.array(end_color.triplet)
    lines = ascii_art.split("\n")
    max_len = max(len(line) for line in lines)
    num_lines = len(lines)
    gradient_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.strip():
                position = (y / num_lines + x / max_len) / 2
                color_rgb = start_rgb + position * (end_rgb - start_rgb)
                color_hex = '#{:02x}{:02x}{:02x}'.format(int(color_rgb[0]), int(color_rgb[1]), int(color_rgb[2]))
                gradient_text.append(char, style=color_hex)
            else:
                gradient_text.append(char)
                
        gradient_text.append("\n")
        
    console.print(gradient_text)
    
    console.print("[bold][red]==================================================================[/red][/bold]")
    
    console.print("\t   𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋")
    
    console.print("   [bold][red]  𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃[/bold][red]")
    
    console.print("[bold][red]==================================================================[/red][/bold]")
    
def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            console.print("[bold][red]==========[/red][ PLAYER DETAILS ][red]==========[/red][/bold]")
            
            console.print(
                f"[bold green] Name   [/bold green]:[bold cyan] {(data.get('Name') if 'Name' in data else 'UNDEFINED')}[/bold cyan].")
                
            console.print(f"[bold green] LocalID[/bold green]:[bold cyan] {data.get('localID')}[/bold cyan].")
            
            console.print(f"[bold green] Money  [/bold green]:[bold cyan] {data.get('money')}[/bold cyan].")
            
            console.print(f"[bold green] Coins  [/bold green]:[bold cyan] {data.get('coin')}[/bold cyan].")
            
        else:
            console.print("[bold red]! ERROR[/bold red]: new accounts most be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print("[bold red]! ERROR[/bold red]: seems like your login is not properly set !.")
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    console.print("[bold][red]========[/red][ ACCESS KEY DETAILS ][red]========[/red][/bold]")
    
    console.print(f"[bold green] Access Key [/bold green]:[bold cyan] {data.get('access_key')}[/bold cyan].")
    
    console.print(f"[bold green ] Telegram ID[/bold green]:[bold cyan] {data.get('telegram_id')}[/bold cyan].")
    
    console.print(f"[bold green] Balance $  [/bold green]:[bold cyan] {(data.get('coins') if not data.get('is_unlimited') else 'Unlimited')}[/bold cyan].")
        
    console.print("[bold][red]======================================[/red][/bold]")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value


def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i + 2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)


def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string


if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold]➤ Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold]➤ Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold]➤ Access Key[/bold]", "Access Key", password=False)
        console.print("[bold cyan]↻ Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMEwan(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]ACCOUNT NOT FOUND[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]WRONG PASSWORD[/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]INVALID ACCESS KEY[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]TRY AGAIN[/bold red].")
                console.print("[bold yellow]! Note:[/bold yellow]: make sure you filled out the fields !.")
                sleep(2)
                continue
        else:
            console.print("[bold green]SUCCESSFUL[/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            console.print("[bold red]{01}[/bold red]: [bold cyan]Increase Money[/bold cyan]           [bold green]1.000K[/bold green]")
            console.print("[bold red]{02}[/bold red]: [bold cyan]Increase Coins[/bold cyan]           [bold green]3.500K[/bold green]")
            console.print("[bold red]{03}[/bold red]: [bold cyan]King Rank[/bold cyan]                [bold green]4.000K[/bold green]")
            console.print("[bold red]{04}[/bold red]: [bold cyan]Change ID[/bold cyan]                [bold green]3.500K[/bold green]")
            console.print("[bold red]{05}[/bold red]: [bold cyan]Change Name[/bold cyan]              [bold green]100[/bold green]")
            console.print("[bold red]{06}[/bold red]: [bold cyan]Change Name (Rainbow)[/bold cyan]    [bold green]100[/bold green]")
            console.print("[bold red]{07}[/bold red]: [bold cyan]Number Plates[/bold cyan]            [bold green]2.000K[/bold green]")
            console.print("[bold red]{08}[/bold red]: [bold cyan]Account Delete[/bold cyan]           [bold green]FREE[/bold green]")
            console.print("[bold red]{09}[/bold red]: [bold cyan]Account Register[/bold cyan]         [bold green]FREE[/bold green]")
            console.print("[bold red]{10}[/bold red]: [bold cyan]Delete Friends[/bold cyan]           [bold green]500[/bold green]")
            console.print("[bold red]{11}[/bold red]: [bold cyan]Unlock Paid Cars[/bold cyan]         [bold green]4000K[/bold green]")
            console.print("[bold red]{12}[/bold red]: [bold cyan]Unlock all Cars[/bold cyan]          [bold green]3.000K[/bold green]")
            console.print("[bold red]{13}[/bold red]: [bold cyan]Unlock all Cars Siren[/bold cyan]    [bold green]2.000K[/bold green]")
            console.print("[bold red]{14}[/bold red]: [bold cyan]Unlock w16 Engine[/bold cyan]        [bold green]3.000K[/bold green]")
            console.print("[bold red]{15}[/bold red]: [bold cyan]Unlock All Horns[/bold cyan]         [bold green]3.000K[/bold green]")
            console.print("[bold red]{16}[/bold red]: [bold cyan]Unlock Disable Damage[/bold cyan]    [bold green]2.000K[/bold green]")
            console.print("[bold red]{17}[/bold red]: [bold cyan]Unlock Unlimited Fuel[/bold cyan]    [bold green]2.000K[/bold green]")
            console.print("[bold red]{18}[/bold red]: [bold cyan]Unlock House 3[/bold cyan]           [bold green]3.500K[/bold green]")
            console.print("[bold red]{19}[/bold red]: [bold cyan]Unlock Smoke[/bold cyan]             [bold green]2.000K[/bold green]")
            console.print("[bold red]{20}[/bold red]: [bold cyan]Change Race Wins[/bold cyan]         [bold green]1.000K[/bold green]")
            console.print("[bold red]{21}[/bold red]: [bold cyan]Change Race Loses[/bold cyan]        [bold green]1.000K[/bold green]")
            console.print("[bold red]{22}[/bold red]: [bold cyan]Clone Account[/bold cyan]            [bold green]5.000K[/bold green]")
            console.print("[bold red]{0} [/bold red]: [bold cyan]Exit[/bold cyan]", end="\n\n")
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            
            
            
            if service == 0: # Exit
                console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                
                
                
            elif service == 1: # Increase Money
                console.print("[bold cyan][!] Insert how much money do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 2: # Increase Coins
                console.print("[bold cyan][!] Insert how much coins do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[bold cyan][%] Giving you a King Rank[/bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 4: # Change ID
                console.print("[bold cyan][!] Enter your new ID.[/bold cyan]")
                new_id = Prompt.ask("[bold][?] ID[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid ID.[/bold yellow]")
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 5: # Change Name
                console.print("[bold cyan][!] Enter your new Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
                    
                    
                    
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan][!] Enter your new Rainbow Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/b
