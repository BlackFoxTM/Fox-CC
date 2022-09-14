import sys
import requests 
import json
from bs4 import BeautifulSoup
from pyfiglet import Figlet 
import colorama
import time
import asyncio
import os
from corex import bin

def detect_os():
    if "win" in sys.platform:
        return "windows"
    else:
        return "linux"


rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN
gg = colorama.Fore.LIGHTCYAN_EX


def logo():
    figlet = Figlet(font="standard").renderText("Fox CC")
    return (gn + figlet)
print (logo())
print (bl + "[-] Powered by Black Fox Security Team ")
print (gn + "[+] Made By Maximum Radikali")
print (cy + "[=] Fox CC Tools Version : 1.1")

opr = input (mag + "\n[x] 1) Generate single valid cc\n[x] 2) Generate multi valid cc (generate cc list)\n[x] 3) CC validator\n[x] 4) Generate Multi Bin Number \n\n[^] Please Enter an option :  ")

def genscard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    card = data['creditCard'][1]
    return (gn + "[-] Brand : %s\n[-] Card Number : %s\n[-] Bank : %s\n[-] Name : %s\n[-] Address : %s\n[-] Country : %s\n[-] Money Range : %s\n[-] CVV : %s\n[-] Expiry : %s\n[-] Pin : %s\n============================\n[*] Telegram Channel : @BlackFoxSecurityTeam" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']) + cv)

def genmcard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    open("generated_card.txt","w").write("")
    for i in range(1,10):
        card = data['creditCard'][i]
        f = open("generated_card.txt","a")
        f.write("[-] Brand : %s\n[-] Card Number : %s\n[-] Bank : %s\n[-] Name : %s\n[-] Address : %s\n[-] Country : %s\n[-] Money Range : %s\n[-] CVV : %s\n[-] Expiry : %s\n[-] Pin : %s\n===================================\n" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']))
    return (gn + "[$] The operation has been success\n[+] Saved File as generated_card.txt" + cv)

def ccvalidator(number , type):
    site = "https://www.tools4noobs.com/"
    payload = {"action":"ajax_credit_card_validate","text":number,"cc":type}
    result = requests.post(site , data=payload)
    soup = BeautifulSoup(result.text ,"html.parser")
    return (bl + soup.text + cv)

if opr == "1":
    print (cy + "[&] You selected first option ! \n\n")
    time.sleep(1)
    print (genscard())
elif opr == "2":
    print (yl + "[&] You selected second option ! \n\n")
    print (genmcard())
elif opr == "3":
    print (mag + "[&] You selected third option !! \n\n")
    number = input(yl + "[$] Please Enter your card number : ")
    if detect_os() == "windows":
        popen = os.popen("node corex\\val.js " + number).read()
        print (bl + popen + cv)
    else:
        popen = os.popen("node corex/val.js " + number).read()
        print (bl + popen + cv)
elif opr == "4":
    print (bl + "[&] You Selected Fourth Option !")
    time.sleep(0.3)
    number = input(gn + "[-] Please Enter Bin Number -  > ")
    round = input(cy + "[+] Pleae Enter Quanity ex : (10) - > ")
    print (rd)
    bin.bin_generator(number , round)
    print ("Saved File as bin_generated.txt !")
    print (mag + "[$] Telegram Channel : @BlackFoxSecurityTeam" + cv)
