import random
from colored import fg
import requests
import sys
import sys as n
import os
import time as mm
import json
import time
from colorama import Fore, init
#TweakPY
color3 = fg(2)
color1 = fg(1)
color2 = fg(50)
colooor = fg(1)
green_color = "\033[1;93m"
O = '\033[33m'  # orange
detect_color = "\033[m"
red_color = "\033[m"
end_banner_color = "\33[00m"
C = "\033[0m"
W = "\033[96m"
BRed="\033[1;31m"
Green="\033[0;36m"
Yellow="\033[0;33m"
count = 0
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)

slow('''

████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
 ╚═██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
          
            Coded By | TweakPY

''')


time.sleep(1)
slow("- CHECKER TIKTOK VERSION 1.05\n")
time.sleep(1)

file = 'user.txt'

slow('[1] EnTer SessionID Manually\n')
slow('[2] Random SessionID\n')
mod = input('[?] Enter Mod :')
if mod == '1':
    print(" ")
    ID = input("Enter Your id Account -> :")
    print(" ")
    tokan = input('Enter Your Bot Tokan -> :')
    print(" ")
    sw = input('Enter SessionId -> :')
    
    if file == "1" or " ":
        file = file
        files = open(file).read().splitlines()

        for files in files:
            url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + files + "&app_language=ar"
            payload = ""
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"
            }
            cookies = {'sessionid': sw}
            response = requests.request("GET", url, data=payload, headers=headers, cookies=cookies)
            post = str(response.json()["status_msg"])
            if post == "" or "":
                count += 1
                print("{}: {}".format(count, files.strip()) + " | Available")
                tele = (f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text=𝙷𝚄𝙽𝚃𝙴𝚁 𝙱𝙾𝚃 ☯︎︎␈\n♡––––––––––––––——♡\n   𝙸 𝙶𝙴𝚃 𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 ☠︎︎ \n♡––––––––––––––——♡\n 𖡃 𝚄𝚂𝙴𝚁 : {files}\n𖡃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @TweakPY\n𖡃 𝙶𝚁𝙾𝚄𝙿 : @sol4o\n♡––––––––––––––——♡')
                r = requests.post(tele)
                with open('usersfound.txt', 'a') as x:
                    x.write(files + '\n')
            else:
                count += 1
                print("{}: {}".format(count, files.strip()) + " | NoT Available")
if mod == '2':

    ID = input("Enter Your id Account -> :")
    print(" ")
    tokan = input('EnTer Your Tokan Bot -> :')
    time.sleep(1)
    use = 'user.txt'
    headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"
    }
    file = open(use, "r") 

    while True:
      Check = file.readline().split('\n')[0]
      tiklog = f'https://www.tiktok.com/@{Check}'
      rq = requests.get(tiklog, headers=headers)
      if rq.status_code == 404:

            count += 1
            print("{}: {}".format(count, Check.strip()) + " | Available")
            tele = (f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text=𝙷𝚄𝙽𝚃𝙴𝚁 𝙱𝙾𝚃 ☯︎︎␈\n♡––––––––––––––——♡\n   𝙸 𝙶𝙴𝚃 𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 ☠︎︎ \n♡––––––––––––––——♡\n 𖡃 𝚄𝚂𝙴𝚁 : {Check}\n𖡃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @TweakPY\n𖡃 𝙶𝚁𝙾𝚄𝙿 : @sol4o\n♡––––––––––––––——♡')
            r = requests.post(tele)
            with open('usersfound.txt', 'a') as x:
             x.write(Check + '\n')

      elif rq.status_code == 200:
          count += 1
          print("{}: {}".format(count, Check.strip()) + " | NoT Available")
          if (Check == ""):
              break

