import os
import sys
import getpass

sX9Q = "UNDERLCTO0L"

g = "\033[92m"
r = "\033[91m"
x = "\033[0m"

os.system("clear")
print(g + """
░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗████████╗██╗░░░██╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║╚══██╔══╝╚██╗░██╔╝
╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║░░░██║░░░░╚████╔╝░
░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░
██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║░░░██║░░░░░░██║░░░
╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
""" + x)

print(g + "🔒 SECURITY SYSTEM 🔒" + x)
print(g + "AUTHORIZED ACCESS ONLY" + x)
print(g + "CONTACT DEVELOPER ON TG @larkinconrad" + x)

u = getpass.getpass("🔐 Enter Security Key: ")

if u != sX9Q:
    print(r + "❌ SECURITY CHECK FAILED ❌" + x)
    sys.exit()

os.system("clear")
print(g + "✅ SECURITY VERIFIED ✅" + x)
print("🔓 Access granted")

print("\n[+] Running your tool...\n")

import os, re, time, json, random
import requests
from faker import Faker
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from datetime import datetime
from rich import print 
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
ua = UserAgent()
faker = Faker()
console=Console()
live = 0
cp = 0
#------------[colour]------------#
R = "[bold red]"
Y = "[bold yellow]"
G = "[bold green]"
B = "[bold blue]"
P = "[bold purple]"
C = "[bold cyan]"
W = "[bold white]"
#---------------------------#
def clear():
    os.system("clear")
#---------------------------#
def logo():
    logx=Panel(f"""{Y}
██╗░░░░░░█████╗░██████╗░██╗░░██╗██╗███╗░░██╗
██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║
██║░░░░░███████║██████╔╝█████═╝░██║██╔██╗██║{R} PREMIUM AUTO CREATE V5
██║░░░░░██╔══██║██╔══██╗██╔═██╗░██║██║╚████║
███████╗██║░░██║██║░░██║██║░╚██╗██║██║░╚███║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝
     """, border_style="bold red")
    print(logx)
  

def fake_password():
    return f"LARKINSUCCESS1738"

def get_temp_email():
    name = faker.first_name()
    domain = random.choice(['gmailos.com', 'hotmail.com','outlook.com','yahoo.com',])
    timestamp = datetime.now().strftime("%H%M%S")
    return f"{name}.{timestamp}@{domain}"

def get_temp_code(email):
    try:
        sess = requests.Session()
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "accept": "application/json",
            "cookie": f"email={email}"
        }
        res = sess.get(f'https://tempmail.plus/api/mails?email={email}&first_id=0&epin', headers=headers)
        data = res.json()

        if data.get("result") and data.get("mail_list"):
            for mail in data["mail_list"]:
                if mail.get("is_new"):
                    subject = mail.get("subject", "")
                    code = re.search(r"(\d+)", subject)
                    return code.group(1) if code else subject
        return None
    except:
        return None

def get_bd_number():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope

def extract_form(html):
    soup = BeautifulSoup(html, 'html.parser')
    return {tag.get("name"): tag.get("value") for tag in soup.find_all("input") if tag.get("name")}

def ugen():
    return ua.random
    
def confirm_id(mail, uid, otp, data, ses, password):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
            'contact': mail,
            'type': "submit",
            'is_soft_cliff': "false",
            'medium': "email",
            'code': otp
        }
        payload = {
            'fb_dtsg': re.search(r'"token":"([^"]+)"', str(data)).group(1),
            'jazoest': re.search(r'name="jazoest" value="(\d+)"', str(data)).group(1),
            'lsd': re.search(r'name="lsd" value="([^"]+)"', str(data)).group(1),
            '__dyn': "",
            '__csr': "",
            '__req': "4",
            '__fmt': "1",
            '__a': "",
            '__user': uid
        }
        headers = {
        'User-Agent': ugen(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            print(Panel(f"{G}[{Y}✓{G}]{W}ID : {R}{uid}", title="DISABLED",border_style="bold green"))
        else:
            cookie = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
            print(Panel(f"{G}[{Y}✓{G}]{W} UID: {G}{uid}\n{G}[{Y}✓{G}]{W} PASS: {G}{password}\n{G}[{Y}✓{G}]{W} COOKIE: {G}{cookie}\n", title="SUCCESS",border_style="bold green"))
            save_result(uid, password, cookie)
    except Exception:
        print(Panel(f"{G}[{Y}✓{G}]{W} OTP Confirmation Failed"))

def register_account():
    global live, cp
    print(Panel(f"{G}CREATING ACCOUNT",border_style="bold green"))
    try:
        ses = requests.Session()
        res = ses.get('https://touch.facebook.com/reg')
        form = extract_form(res.text)
        fname, lname = faker.first_name(), faker.last_name()
        phone = get_bd_number()
        email = get_temp_email()
        password = fake_password()
        payload = {
        'ccp': '2',
        'reg_instance': form.get('reg_instance'),
        'reg_impression_id': form.get('reg_impression_id'),
        'logger_id': form.get('logger_id'),
        'firstname': fname,
        'lastname': lname,
        'birthday_day': str(random.randint(1, 28)),
        'birthday_month': str(random.randint(1, 12)),
        'birthday_year': 2004,
        'reg_email__': email,
        'reg_passwd__': password,
        'sex': '2',
        'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
        'submit': 'Sign Up',
        'fb_dtsg': form.get('fb_dtsg', ''),
        'jazoest': form.get('jazoest'),
        'lsd': form.get('lsd'),
        '__dyn': '', '__csr': '', '__req': 'q', '__a': '', '__user': '0'
        }
        headers = {'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugen(),
                'viewport-width': '980'
            
        }
        reg = ses.post('https://m.facebook.com/reg/submit/', data=payload, headers=headers)
        cookies = ses.cookies.get_dict()
        if "c_user" in cookies:
        uid = cookies["c_user"]
        print(f"{G}[{Y}✅{G}]{W} ALIVE UID CREATED: {G}{uid}\n{G}[{Y}🔑{G}]{W} PASSWORD: {G}{password}")
        code = get_temp_code(email)
        time.sleep(3)
        print(f"{G}[{Y}🔑{G}] CODE  : {code}")
        if code:
        confirm_id(email, uid, code, reg.text, ses, password)
    else:
        print(f"{R}⚠️ OTP not received for: {email}")
    live += 1
else:
    print(f"{R}Failed Checkpoint 🚨")
    cp += 1
except requests.exceptions.ConnectionError:
    print(f"{R}(!!) Internet Connection Error!")
    time.sleep(2)
    exit(1)

        
def main():
    clear()
    logo()
    info = f"""
    {G}[{Y}✅{G}]{W} DEVELOPER : {G}Lrkin Conrd
    {G}[{Y}✅{G}]{W} OWNER : {G}??? 
    {G}[{Y}✅{G}]{W} WARNING : {G}STRICTLY 1 DEVICE! 
    """
    print(Panel(info,border_style="bold red"))
    total = Prompt.ask(f"{G}[{Y}✅{G}]{W} Enter Account Create Limit  ")
    clear()
    logo()
    print(Panel(info,border_style="bold green"))
    for _ in range(int(total)):
        register_account()
    print(Panel(f"{G}[{Y}✅{G}]{W} TOTAL SUCCESS: {G}{live}\n{G}[{Y}❌{G}]{W} FAILED: {R}{cp}",border_style="bold green"))

if __name__ == "__main__":
    main()
