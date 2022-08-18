from pystyle import *
import os
import time
import threading
from colorama import Fore,init
import requests, random, string
from random import choice

try:
    import requests, random, string
except ImportError:
    input("Error while importing modules.")
    exit()
    
class spotify:

    def __init__(self, profile, proxy = None):
        self.session = requests.Session()
        self.profile = profile
        self.proxy = proxy
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
        }
        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
        proxies = None
        if self.proxy != None:
            proxies = {"https": f"http://{self.proxy}"}
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname=github.com/ZeusFuckYou/Aspic&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        try:
            create = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data, proxies = proxies)
            if "login_token" in create.text:
                login_token = create.json()['login_token']
                return login_token
            else:
                return None
        except:
            return False

    def get_csrf_token(self):
        try:
            r = self.session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return None
        
    def get_token(self, login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "WebPlayer",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None

    def follow(self):
        if "/user/" in self.profile:
            self.profile = self.profile.split("/user/")[1]
        if "?" in self.profile:
            self.profile = self.profile.split("?")[0]
        login_token = self.register_account()
        if login_token == None:
            return None, "while registering, ratelimit"
        elif login_token == False:
            if self.proxy == None:
                return None, f"unable to send request on register"
            return None, f"bad proxy on register {self.proxy}"
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "while getting auth token"
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "app-platform": "WebPlayer",
            "Referer": "https://open.spotify.com/",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "authorization": "Bearer {}".format(auth_token),
        }
        try:
            self.session.put(
                "https://api.spotify.com/v1/me/following?type=user&ids=" + self.profile,
                headers = headers
            )
            return True, None
        except:
            return False, "while following"





lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0

text = r'''
 _______ _______  _____  _____ _______
 |_____| |______ |_____]   |   |      
 |     | ______| |       __|__ |_____ 
                                      '''

banner = r'''
              ---_ ......._-_--.
              (|\ /      / /| \  \
              /  /     .'  -=-'   `.
             /  /    .'             )
           _/  /   .'        _.)   /
          / o   o        _.-' /  .'
          \          _.-'    / .'*|
           \______.-'//    .'.' \*|
            \|  \ | //   .'.' _ |*|
             `   \|//  .'.'_ _ _|*|
              .  .// .'.' | _ _ \*|
              \`-|\_/ /    \ _ _ \*\
               `/'\__/      \ _ _ \*\
              /^|            \ _ _ \*
             '  `             \ _ _ \      
                               \_
'''



banner = Add.Add(text, banner, center=True)

def tui():
    System.Clear()
    print()
    print(Colorate.Diagonal(Colors.DynamicMIX([Colors.light_green, Colors.dark_green, Colors.light_gray, Colors.dark_gray]), Center.XCenter(banner)))
    System.Title("Aspic")
    print()
    print(f" {Col.Symbol('-_-', Col.dark_green, Col.dark_gray)} {Col.light_green}Aspic{Col.dark_gray} - The {Col.light_green}best tools{Col.dark_gray} to upgrade your {Col.light_green}Spotify{Col.dark_gray} Account{Col.reset} ")
    print()
    print(f" {Col.Symbol('<3', Col.dark_green, Col.dark_gray)} {Col.dark_gray}Go to {Col.dark_green}github.com/ZeusFuckYou/Aspic{Col.dark_gray} to download this tool{Col.dark_green} !{Col.reset} ")
    print('\n')

  
tui()
spotify_profile = str(input(f" {Col.Symbol('?', Col.light_green, Col.light_gray)} {Col.light_gray}Paste your Account Link {Col.light_green}->{Col.reset} "))
print("")
threads = int(input(f" {Col.Symbol('?', Col.light_green, Col.light_gray)} {Col.light_gray}Threads {Col.dark_gray}( 1000 max ){Col.light_green} ->{Col.reset} "))
print(f'\n [{Col.dark_gray}1{Col.reset}] Proxies\n [{Col.dark_gray}2{Col.reset}] Proxyless')
print("")
option = int(input(f" {Col.Symbol('?', Col.light_green, Col.light_gray)} {Col.light_gray}Choice {Col.light_green}->{Col.reset} "))

def load_proxies():
  if not os.path.exists("proxies.txt"):
      print(f"\n {Col.Symbol('!', Col.light_green, Col.light_gray)} {Col.dark_gray}File {Col.light_green}proxies.txt {Col.dark_gray}not found{Col.reset}")
      time.sleep(3)
      exit()
  with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print(f"\n {Col.Symbol('!', Col.light_green, Col.light_gray)} {Col.dark_gray}No proxies loaded in {Col.light_green}proxies.txt{Col.reset}")
            time.sleep(3)
            exit()

if option not in [1,2]:
    print(f'{Col.dark_gray} Please enter a {Col.light_green}valid{Col.dark_gray} option')
    time.sleep(5)

if option == 1:
  load_proxies()

if option == 2:
  print(f"\n {Col.Symbol('!', Col.light_green, Col.light_gray)} {Col.dark_gray}This option is not {Col.light_green}available{Col.dark_gray} for the moment")
  time.sleep(5)
  exit()



def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        print(f"\n{Col.light_gray} Followed {Col.light_green}{counter}{Col.reset} ( {Col.dark_gray}{spotify_profile} ){Col.reset}")


while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: 
            proxy_counter = 0
    
  



       




    