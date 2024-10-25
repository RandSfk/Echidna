import os
from requests.api import head
try:
    import requests
except ImportError:
    print("Module requests tidak terinstall, install module terlebih dahulu.")
    os.system("pip install requests")
try:
    import rich
except ImportError:
    print("Module rich tidak terinstall, install module terlebih dahulu.")
    os.system("pip install rich")
import json
import re
import sys
from rich import print
from rich.panel import Panel
from rich.columns import Columns
import random
import string
import time
import requests as req
import platform

class Echidna:
    def __init__(self):
        self.proxies = self.get_proxies()
        self.requests=req.Session()
        self.requests.impersonate='chrome110'
    def get_proxies(self):
        proxies = [
            {"ip": "54.67.125.45", "port": 3128},
            {"ip": "72.10.164.178", "port": 31619},
            {"ip": "72.10.164.178", "port": 2343},
            {"ip": "158.255.212.55", "port": 7839},
            {"ip": "67.43.236.19", "port": 1223},
            {"ip": "8.213.129.20", "port": 13},
            {"ip": "8.213.129.20", "port": 9098},
            {"ip": "8.213.129.20", "port": 9992},
            {"ip": "8.213.129.20", "port": 1029},
            {"ip": "8.130.36.245", "port": 9000},
            {"ip": "47.99.112.148", "port": 3128},
            {"ip": "152.32.173.226", "port": 8198},
            {"ip": "181.78.94.157", "port": 999},
            {"ip": "181.209.82.197", "port": 999},
            {"ip": "103.143.196.67", "port": 8080},
            {"ip": "103.166.194.114", "port": 8080},
            {"ip": "181.209.125.122", "port": 999},
            {"ip": "103.209.38.132", "port": 81},
            {"ip": "161.34.40.32", "port": 3128},
            {"ip": "190.192.45.168", "port": 3128},
            {"ip": "161.34.40.113", "port": 3128},
            {"ip": "94.158.155.138", "port": 54698},
            {"ip": "27.147.140.129", "port": 58080},
            {"ip": "182.53.143.20", "port": 8180},
            {"ip": "103.80.224.33", "port": 83},
            {"ip": "103.143.105.138", "port": 8080},
            {"ip": "201.157.61.166", "port": 999}
        ]
        return random.choice(proxies)

    def load_hasil():
        file_name = 'hasil.json'
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                try:
                    data = json.load(file)
                    return data.get('accounts', [])
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_hasil(new_data):
        file_name = 'hasil.json'
        
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {'accounts': []}
        else:
            data = {'accounts': []}

        data['accounts'].append(new_data['account'])

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def get_headers(self, Country, Language):
        while True:
            try:
                an_agent = f'Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111, 999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
                res = requests.get("https://www.facebook.com/", headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}, proxies=self.proxies, timeout=30)
                with open('dump.txt', 'w') as f:
                    f.write(res.text)
                if 'datrCookie:' in res.text:
                    js_datr = re.search('datrCookie:"(.*?)"', res.text).group(1)
                else:
                    raise ValueError("Failed to find '_js_datr' in response.")
                
                r = requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers={'user-agent': an_agent}, proxies=self.proxies, timeout=30).cookies
                
                if 'csrftoken' not in r or 'mid' not in r or 'ig_did' not in r:
                    raise ValueError("Required cookies are missing.")
                
                headers1 = {
                    'authority': 'www.instagram.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': an_agent,
                    'viewport-width': '980',
                }
                response1 = requests.get('https://www.instagram.com/', headers=headers1, proxies=self.proxies, timeout=30)
                
                # Cek apakah appid dan rollout ada
                if 'APP_ID":"' in response1.text and 'rollout_hash":"' in response1.text:
                    appid = response1.text.split('APP_ID":"')[1].split('"')[0]
                    rollout = response1.text.split('rollout_hash":"')[1].split('"')[0]
                else:
                    raise ValueError("Failed to find 'APP_ID' or 'rollout_hash' in response.")
                
                headers = {
                    'authority': 'www.instagram.com',
                    'accept': '*/*',
                    'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/accounts/signup/email/',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': an_agent,
                    'viewport-width': '360',
                    'x-asbd-id': '198387',
                    'x-csrftoken': r["csrftoken"],
                    'x-ig-app-id': str(appid),
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': str(rollout),
                    'x-requested-with': 'XMLHttpRequest',
                    'x-web-device-id': r["ig_did"],
                }
                return headers
            except Exception as e:
                print("Error:", e)

    def tunggu(pesan="Sedang memproses", interval=0.5, hitungan=10):
        angka = hitungan
        while angka > 0:
            sys.stdout.write(f"\r{pesan}... {angka}")
            sys.stdout.flush()
            angka -= 1
            time.sleep(interval)
        sys.stdout.write("\r" + " " * (len(pesan) + len(str(hitungan)) + 5) + "\r")  # Bersihkan garis
        sys.stdout.flush()

    def cgpp(coki, self):
        header = {
            "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
            "x-csrftoken":coki['csrftoken'],
            'x-instagram-ajax':'1017598993',
            'x-requested-with':'XMLHttpRequest'
        }
        files = {'profile_pic': open("pp.jpg",'rb')}
        values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg",
    "Content-Type": "image/jpeg"}
        self.tunggu("Mengubah foto profile",0.5,10)
        res = req.post('https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/',headers=header, files=files, data=values, cookies=coki)
        if res and 'has_profile_pic":"true' in res.text:
            print("Berhasil Mengubah Profile")
            return True
        else:
            print("Gagal Mengubah Profile")
            return False

    def Get_UserName(Headers,Name,Email,self):
        try:

            updict = {"referer": 'https://www.instagram.com/accounts/signup/birthday/'}
            Headers = {key: updict.get(key, Headers[key]) for key in Headers}
            while True:


                data = {
                    'email': Email,
                    'name': Name+str(random.randint(1,99)),
                }

                response = requests.post(
                    'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                    headers=Headers,
                    data=data,
                    proxies=self.proxies,
                    timeout=30
                )
                if 'status":"fail' in response.text:
                    print("Fail to get username")
                    sys.exit()
                elif 'status":"ok' in response.text :
                    return random.choice(response.json()['suggestions'])
                else:print(response.text)

        except Exception as E:
            print(E)


    def Send_SMS(self, Headers,Email):
        try:
            data = {
                'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
                'email': Email,
    }

            response = requests.post(
                'https://www.instagram.com/api/v1/accounts/send_verify_email/',
                headers=Headers,
                data=data,
                proxies=self.proxies,
                timeout=30
            )
            return response.text
        except Exception as E:
            print(E)



    def Validate_Code(self, Headers,Email,Code):

        try:
            updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
            Headers = {key: updict.get(key, Headers[key]) for key in Headers}



            data = {
                'code': Code,
                'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
                'email': Email,
            }

            response = requests.post(
                'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
                headers=Headers,
                data=data,
                proxies=self.proxies,
                timeout=30
            )
            return response

        except Exception as E:
            print(E)

    def get_firstname(self):
        indonesian_names = [
            "Budi", "Siti", "Agus", "Rina", "Dewi", "Eko", "Putri", "Joko", "Fitri", "Hendra",
            "Wati", "Santoso", "Adi", "Lestari", "Darto", "Maya", "Samsul", "Kartini", "Rahmat", "Endang",
            "Nur", "Widodo", "Teguh", "Sri", "Suryo", "Hadi", "Tuti", "Iwan", "Yanto", "Lia",
            "Rizki", "Sari", "Arif", "Yuni", "Febri", "Asep", "Dian", "Fajar", "Gunawan", "Ismail"
        ]

        european_names = [
            "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Wilson", "Martin", "White", "Clark", "Harris",
            "Lewis", "Walker", "Robinson", "Wood", "Thompson", "Hall", "Wright", "Green", "Adams", "Baker",
            "King", "Scott", "Phillips", "Evans", "Turner", "Carter", "Collins", "Cook", "Parker", "Edwards",
            "Morris", "Mitchell", "Bell", "Ward", "Cooper", "Morgan", "Rogers", "Reed", "Gray", "Howard",
            "Russell", "Hughes", "Campbell", "Murphy", "Stewart", "Foster", "Simmons", "Ellis", "Jenkins", "Ross"
        ]
        
        first_name = random.choice(indonesian_names)
        last_name = random.choice(european_names)
        
        return f"{first_name}{last_name}"

    def Create_Acc(self, Headers,Email,SignUpCode):
        try:
            #firstname=Email.split("@")[0].capitalize()+get_firstname()
            firstname= self.get_firstname()
            UserName=firstname.lower()+str(random.randint(0,999))
            Password="$Mantapkali27"
            updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
            Headers = {key: updict.get(key, Headers[key]) for key in Headers}
            data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
                'email': Email,
                'username': UserName,
                'first_name': firstname,
                'month': random.randint(1,12),
                'day': random.randint(1,28),
                'year': random.randint(1990,2001),
                'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
                'seamless_login_enabled': '1',
                'tos_version': 'row',
                'force_sign_up_code': SignUpCode,
            }
            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
                headers=Headers,
                data=data,
                timeout=30
            )
            account = {}
            cookies = {}
            if '"account_created":true' in response.text:
                account['email'] = Email
                account['username'] = UserName
                account['password'] = Password
                cookies['sessionid'] = response.cookies.get('sessionid', 'N/A')
                cookies['csrftoken'] = response.cookies.get('csrftoken', 'N/A')
                cookies['ds_user_id'] = response.cookies.get('ds_user_id', 'N/A')
                cookies['ig_did'] = response.cookies.get('ig_did', 'N/A')
                cookies['rur'] = response.cookies.get('rur', 'N/A')
                cookies['mid'] = Headers['cookie'].split('mid=')[1].split(';')[0] if 'mid=' in Headers['cookie'] else 'N/A'
                cookies['datr'] = Headers['cookie'].split('datr=')[1] if 'datr=' in Headers['cookie'] else 'N/A'
                account['status'] = "OK"
                account['str_cookies'] = " ".join([f"{key}={value};" for key, value in cookies.items()])
            else:
                account['email'] = Email
                account['username'] = UserName
                account['password'] = Password
                cookies['mid'] = Headers['cookie'].split('mid=')[1].split(';')[0] if 'mid=' in Headers['cookie'] else 'N/A'
                cookies['datr'] = Headers['cookie'].split('datr=')[1] if 'datr=' in Headers['cookie'] else 'N/A'
                account['status'] = "FAIL"
            account['cookies'] = cookies
            return account
        except Exception as E:
            print(E)
            return None

    def get_public_ip(self):
        response = requests.get("https://api64.ipify.org?format=json")
        ip_address = response.json()["ip"]
        return ip_address

    def logo(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            pass

        author = "[white]Author: Rand Sfk"
        version = "[white]Version: 1.0.0"
        separator = "[green]-" * 80
        logos = f"""[green]
    ░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░  
    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
    ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░"""
        combine = f"{logos}\n{separator}\n                          {author}  [green]|  {version}\n{separator}"
        print(Panel(combine, style="bold green", width=90, title="Echidna", subtitle="[italic]Multi Create Instagram Account"))
        device = self.get_device_info()
        profile = f"""[white]    System    : {device['System']}{device['Release']}
        Processor : {device['Machine']}
        Node      : {device['Node Name']}"""
        system = Panel(profile, style="bold green", width=45)
        user = f"""[white]    IP Address    : {self.get_public_ip()}
        Ranks         : Free
        LICENSE       : Free"""
        users = Panel(user, style="bold green", width=45)
        print(Columns([system, users]))

    def get_device_info(self):
        system = platform.system()
        node = platform.node()
        release = platform.release()
        version = platform.version()
        machine = platform.machine()
        processor = platform.processor()
        device_info = {
            "System": system,
            "Node Name": node,
            "Release": release,
            "Version": version,
            "Machine": machine,
            "Processor": processor
        }
        return device_info

    def akun_baru(self):
            try:
                headers=self.get_headers(Country='US',Language='en')
                Email=input("Masukkan email anda: ")
                ss=self.Send_SMS(headers,Email)
                if 'email_sent":true' in ss:
                    time.sleep(5)
                    code=input("Masukkan Kode: ")
                    a=self.Validate_Code(headers,Email,code)
                    if 'status":"ok' in a.text:
                        SignUpCode=a.json()['signup_code']
                        print(headers, Email, SignUpCode)
                        post = self.Create_Acc(headers,Email,SignUpCode)
                        print(post)
                        if post and post['status'] == "OK":
                            ubah_pp = self.cgpp(post['cookies'])
                            if ubah_pp:
                                self.save_hasil({"account":post})
                                self.cetak(post, 'ok')
                            else:
                                self.cetak(post, 'no')
                                self.akun_baru()
                        else:
                            print("[red]Failed to created account\nName:", Email)
                            self.akun_baru()
                    else:
                        print(a.text)
                else :
                    print("Fail..")
            except Exception as e:
                print("[bold red]Error in: ",e)

    def main(self):
        self.logo()
        print(Panel("[bold white]1. Create Account\n[bold white]2. Load Account", style="bold green", width=30))
        pilih = input("Pilih: ")
        if pilih == "1":
            self.akun_baru()

        elif pilih == "2":
            pa = self.load_hasil()
            for i in pa:
                self.cetak(i)
        else:
            print("[bold red]Pilihan tidak ada")
        

    def get_email(username):
        url = "https://temp-mail-api3.p.rapidapi.com/email/random"

        headers = {
            'x-rapidapi-host': 'temp-mail-api3.p.rapidapi.com',
            'x-rapidapi-key': '62a289a275msh754c53be3f6aad3p13a1e6jsnc3fc8109d15d',
        }
        response = requests.get(url, headers=headers)
        if response.get("status") == "success":
            email = response['email']
            return email

    def get_code(email):
        try:
            url = f"https://temp-mail-api3.p.rapidapi.com/message/{email}"
            headers = {
            'x-rapidapi-host': 'temp-mail-api3.p.rapidapi.com',
            'x-rapidapi-key': '62a289a275msh754c53be3f6aad3p13a1e6jsnc3fc8109d15d',
            }
            response = requests.get(url, headers=headers)
            print(response.json())
        except Exception:
            return None

    def cetak(data, tipe="ok"):
        if tipe == "ok":
            status_text = "[bold green]Success[/bold green]"
            status_color = "green" if data.get('status') == "OK" else "red"
            user_info = f"[bold green]Email:[/bold green] {data['email']}\n" \
                        f"[bold green]Username:[/bold green] {data['username']}\n" \
                        f"[bold green]Password:[/bold green] {data['password']}"

            cookies_info = " ".join([f"{key}={value};" for key, value in data['cookies'].items()])
            combined_info = f"{user_info}\n[bold green]Cookies: {cookies_info}"
            print(combined_info)
            print('-'*100)

        elif tipe == "no":
            status_text = "[bold red]Failed[/bold red]"
            status_color = "red" if data.get('status') == "OK" else "red"
            user_info = f"[bold red]Email:[/bold red] {data['email']}\n" \
                        f"[bold red]Username:[/bold red] {data['username']}\n" \
                        f"[bold red]Password:[/bold red] {data['password']}"

            cookies_info = " ".join([f"{key}={value};" for key, value in data['cookies'].items()])
            combined_info = f"{user_info}\n[bold red]Cookies: {cookies_info}"
            print('-'*100)
            print(combined_info)
            print('-'*100)

    def follow(self):
        db = self.load_hasil()
        for i in db:
            url = "https://igfollower.net/girisyap"
            if "igfolcok" in i:
                continue
            else:
                rques = req.Session()
                data = {
                    "username": i['username'],
                    "password": i['password'],
                }
                respon = rques.post(url, data=data)
                rspon = respon.json()
                print(rspon)
                if rspon.get('status') == "success":
                    print(f"[bold green]Login Success: {i['username']}")
                    igfolcok = respon.cookies.get_dict()
                    i['igfolcok'] = igfolcok
                    self.save_hasil(db)

                elif "User Not Found" in rspon.get("error"):   
                    print(f"[bold red]Login Failed(Can't Find Account): @{i['username']}")
                    continue

                elif "checkpoint." in rspon.get("error"):
                    print(f"[bold yellow]Login Failed(Checkpoint): @{i['username']}")
                    igfolcok = respon.cookies.get_dict()
                    payload = rspon.get("allData")
                    verif = req.post("https://igfollower.net/ajax/kod-gonder", data=payload, cookies=igfolcok)
                    print(verif.text, verif.cookies.get_dict())
                    continue
            
if __name__ == "__main__":
    a = Echidna()
    a.main()
