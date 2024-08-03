import os,sys,random
import platform
try:
    import httpx
    from colr import color
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = httpx.get('https://api.ipify.org').text
    response = httpx.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    print(f"problem : {e}")
    input("lets Fix it?... Press Enter")
    def is_termux():
        return 'termux' in platform.system().lower()

    if is_termux():
        print("Python is running in Termux.")
        os.system("pkg update && pkg upgrade -y")
        os.system("termux-setup-storage -y")
    else:
        print("Python is running on a Linux PC.")
    os.system("pip install colr")
    os.system("pip install httpx")
    os.system("pip install pystyle")
    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem

VERSION_CHECK_URL = f"{server_online}/termux-version"

def get_latest_version_info():
    try:
        response = httpx.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    with httpx.Client(follow_redirects=True) as client:
        response = client.get(download_url)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)

def update_script():
    version_info = get_latest_version_info()
    if not version_info:
        return
    
    latest_version = version_info.get("version")
    download_url = version_info.get("download_url")
    print(f"CURRENT_VERSION {CURRENT_VERSION}\nlatest_version {latest_version}\ndownload_url {download_url}")
    if latest_version and download_url:
        if latest_version != CURRENT_VERSION:
            print(f"New version available: {latest_version}")
            print(f"Downloading update... {download_url}")
            download_new_version(download_url, sys.argv[0])
            print("Script updated to the latest version. Please restart the script.")
            exit()
        else:
            print("You already have the latest version.")
    else:
        print("Invalid version information received.")
update_script()


def disp(clrnama):
    clrfirsttime = True
    clrVnama = clrnama.split("[")
    clrdisps = clrVnama[0]
    for clrx in clrVnama:
        if clrfirsttime == False:
            clrcode1 = f"{clrx[0:2]}"
            clrcode2 = f"{clrx[2:4]}"
            clrcode3 = f"{clrx[4:6]}"
            clrcode1 = (int(clrcode1, 16))
            clrcode2 = (int(clrcode2, 16))
            clrcode3 = (int(clrcode3, 16))
            clrhuruf = clrx[7:8]
            clrdisps += color(clrhuruf,
                              fore=(clrcode1,
                                    clrcode2,
                                    clrcode3),
                              back=(0, 0, 0))
        if clrfirsttime:
            clrfirsttime = False

    clrdisps += clrVnama[len(clrVnama)-1][8:len(clrVnama[len(clrVnama)-1])]
    return(clrdisps)

warnasekarang=""
def generate(namax):
    global warnasekarang
    gabungwarna = ""
    contohnama = namax
    # proses memecah huruf di nama
    data = {
        "huruf": "",
        "kodewarna": [255, 0, 0],
        "mode": 1,
        "kodewarnaCPM": ""
    }
    while True:
        while True:
            tanya = random.choice(["merah","kuning","hijau","biru","ungu","pink"])
            if tanya!=warnasekarang:
                warnasekarang = tanya
                break
        if tanya == "merah":
            data["kodewarna"] = [255, 0, 0]
            break
        elif tanya == "kuning":
            data["kodewarna"] = [230, 245, 66]
            break
        elif tanya == "hijau":
            data["kodewarna"] = [0, 255, 0]
            break
        elif tanya == "biru":
            data["kodewarna"] = [0, 0, 255]
            break
        elif tanya == "ungu":
            data["kodewarna"] = [150, 66, 245]
            break
        elif tanya == "pink":
            data["kodewarna"] = [245, 66, 215]
            break
        else:
            print("Harus sesuai pilihan warna ..!")

    for huruf in contohnama:
        while True:
            # print(f"\nmode sekarang : {data['mode']}")
            tambah = 45
            if data["mode"] == 1:
                if data["kodewarna"][1]+tambah <= 255:
                    data["kodewarna"][1] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 255, 0]
            elif data["mode"] == 2:
                if data["kodewarna"][0]-tambah >= 0:
                    data["kodewarna"][0] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 0]
            elif data["mode"] == 3:
                if data["kodewarna"][2]+tambah >= 255:
                    data["kodewarna"][2] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 255, 255]
            elif data["mode"] == 4:
                if data["kodewarna"][1]-tambah >= 0:
                    data["kodewarna"][1] -= tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [0, 0, 255]
            elif data["mode"] == 5:
                if data["kodewarna"][0]+tambah >= 255:
                    data["kodewarna"][0] += tambah
                    break
                else:
                    data["mode"] += 1
                    data["kodewarna"] = [255, 0, 255]
            elif data["mode"] == 6:
                if data["kodewarna"][2]-tambah >= 255:
                    data["kodewarna"][2] -= tambah
                    break
                else:
                    data["mode"] = 1
                    data["kodewarna"] = [255, 0, 0]
        # print(f"{huruf} {data['kodewarna']}")
        gabungwarna += color(huruf,
                             fore=(data["kodewarna"][0],
                                   data["kodewarna"][1],
                                   data["kodewarna"][2]),
                             back=(0, 0, 0))
        kodas = []
        for t in range(3):
            clrcode = hex(data["kodewarna"][t])[2::]
            if len(clrcode) == 1:
                clrcode += "0"
            kodas.append(clrcode)
        data["kodewarnaCPM"] += f"[{kodas[0]}{kodas[1]}{kodas[2]}]{huruf}"
    # print(f"hasil\t:  {disp(data['kodewarnaCPM'])}")
    # print(f"kode\t:  {data['kodewarnaCPM']}")
    return data["kodewarnaCPM"]
def refresh_x():
    import inspect
    kucing_garong = inspect.getfile(inspect.currentframe())
    with open(kucing_garong, 'r') as file:
        gajah_terbang = file.read()
        gajah_duduk = len(gajah_terbang)
    if debug_mode!=1: 
            pass
    return gajah_duduk
pySystem.Clear()
pySystem.Size(80, 40)


text = """
< [ YouTube TopixSB ] > X < [ ₱ⱤØ₲Ɽ₳₥ ฿Ɇ₮₳ ] >"""[1:]

banner = r"""
___ç$$$ç________________
__$$$$$$$_####______####_       YouTube TopixSB
___*$$$$$$ç####___########        
_____*$$$$$$$$$$$##########     ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█
_____$$$$$$$$$$$$$##########    ░▒█░░ ░▀▀▀▄▄ ▒█▀▀▄
______$$$$$$$$$$$$$##########   ░▒█░░ ▒█▄▄▄█ ▒█▄▄█ 
______$$$$$$$$$$_$$$##########
______$$$$$$$$$$##$$$##########
_______$$$$$$$$$_##$$##########
______$$$$$$$$$$___$$#########
_____$_$$$$$$$$$$__$$_########
___$$__$$$$$$$$$$_$$$__######
______$$$$$$$$$$__$$$___#####
______$$$$$$$$$___$$____####
______$$$$$$$$$_________###
______$$$$$$$$__________##
_______$$$$$$___________##
_______$$$$$$______________
_______$$$$$$$$____________
_______$$$$$$$$____________
_______$$$$_$$$$___________
_______$$$$_$$$$___________
_______$$$___$$$$__________
__ççç$$$$$$_çç$$$$__________       
                          
           Car Parking Multiplayer Instant Script
                    LESS THEN 1 MINUTE

                        PRESS ENTER          
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.purple_to_red, pyColorate.Vertical, enter=True)

pySystem.Clear()

print("\n"*2    )
print(pyColorate.Horizontal(pyColors.red_to_yellow, pyCenter.XCenter(text)))
print("\n"*2)


delet=["cpm/pos.py","cpm/__init__.py"]
for psdd in delet:
    if os.path.exists(f"{psdd}") == True:
        os.system(f"rm {psdd}")



def c(colr, tex):
    try:
        w = {
            "RED": [255, 0, 0],
            "GREEN": [0, 255, 0],
            "CYAN": [0, 255, 255],
            "YELLOW": [255, 255, 0],
            "GOLD": [255, 223, 0]
        }
        return color(tex,
                     fore=(w[colr.upper()][0],
                           w[colr.upper()][1],
                           w[colr.upper()][2]),
                     back=(0, 0, 0))
    except:
        return tex
    
def heder():
        pySystem.Clear()
        print(f"build : {refresh_x()}")
        versi_tampil = disp(generate(f"Topix SB CPM TOOLS {CURRENT_VERSION}"))
        loc_info = f"  Location\t: {data_jaringan.get('city')}, {data_jaringan.get('region')}, {data_jaringan.get('country')}"
        loc_info = pyColorate.Horizontal(pyColors.green_to_yellow, loc_info)
        isp_info = f"  ISP     \t: {data_jaringan.get('org')}"
        isp_info = pyColorate.Horizontal(pyColors.green_to_yellow, isp_info)
        bannerwz = f"""{c("cyan","=======================================================================")}
  {versi_tampil} {c("cyan","||")} {c("green","https://carparking.topixsb.dev/")}
{c("cyan","=======================================================================")}
{loc_info}
{isp_info}"""
        print(bannerwz)

tex="""     IMPORTANT READ

    You must log out of the CPM application first, 
    unless you only want to use the "Inject Rank" and "Instant Rank" features, 
    as these two features do not require you to log out.

    Please refill your cash only at https://carparking

"""

print(pyColorate.Horizontal(pyColors.green_to_yellow, pyCenter.XCenter(tex)))



def warnain(text,inpo=""):
    tex = f"""{c("cyan","=======================================================================")}"""
    if inpo:
        tex+=f"\n\t\t{pyColorate.Horizontal(pyColors.red_to_purple, inpo)}"
    tex+=f"""
{pyColorate.Horizontal(pyColors.green_to_yellow, text)}
{c("cyan","=======================================================================")}"""

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMEwan(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'ACCOUNT NOT FOUND.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY[/bold red].'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN.'))
                print(Colorate.Horizontal(Colors.rainbow, '! Note: make sure you filled out the fields !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: Increase Money           1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: Increase Coins           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: King Rank                4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: Change ID                3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: Change Name              1.00'))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: Change Name (Rainbow)    1.00'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: Number Plates            2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: Account Delete           FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: ccount Register          FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: Delete Friends           5.00'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: Unlock Paid Cars         4.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: Unlock all Cars          3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: Unlock all Cars Siren    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: Unlock w16 Engine        3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: Unlock All Horns         3.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: Unlock Disable Damage    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: Unlock Unlimited Fuel    2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: Unlock House 3           3.500K'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: Unlock Smoke             2.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: Change Race Wins         1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: Change Race Loses        1.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: Clone Account            5.000K'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : Exit'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much money do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much coins do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Rainbow Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] After deleting your account there is no going back !!.'))
                answ = Prompt.ask("[?] Do You want to Delete this Account ?!", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] Registring new Account.'))
                acc2_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Creating new Account: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: In order to tweak this account with CPMEwan.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'you most sign-in to the game using this account.'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'This email is already exists !.'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Deleting your Friends: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Note: this function takes a while to complete, please don't cancel.", end=None)
                console.print("[%] Unlocking All Paid Cars: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Unlocking All Cars: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Unlocking All Cars Siren: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Unlocking w16 Engine: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Unlocking All Horns: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 20: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 21: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you lose.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 22: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] Please Enter Account Detalis.'))
                to_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                to_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            else: continue
            break
        break
