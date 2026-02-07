#code by lrkn
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
console = Console()
live = 0
cp = 0

R = "[bold red]"
Y = "[bold yellow]"
G = "[bold green]"
B = "[bold blue]"
P = "[bold purple]"
C = "[bold cyan]"
W = "[bold white]"

def clear():
    os.system("clear")

def logo():
    logx = Panel(f"""{Y}
██╗░░░░░░█████╗░██████╗░██╗░░██╗██╗███╗░░██╗
██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║
██║░░░░░███████║██████╔╝█████═╝░██║██╔██╗██║
██║░░░░░██╔══██║██╔══██╗██╔═██╗░██║██║╚████║
███████╗██║░░██║██║░░██║██║░╚██╗██║██║░╚███║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝{R}V1
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
            'priority': "u=1, i"
        }
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            print(f"{uid}|{password}")
        else:
            cookie = ";".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
            print(f"{uid}|{password}")
            save_result(uid, password, cookie)
    except Exception:
        print(f"{uid}|{password}")

def register_account():
    global live, cp
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
            print(f"{uid}|{password}")
            code = get_temp_code(email)
            time.sleep(3)
