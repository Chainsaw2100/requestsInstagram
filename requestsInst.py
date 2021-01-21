import requests
import json
import os
import re
from datetime import datetime
from time import sleep

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'
time = int(datetime.now().timestamp())
payload = {
    'username': 'somethingtoldme@yandex.ru',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:314539314539b',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

glob_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest", "Referer": "https://www.instagram.com/accounts/login/"}


def head_like():
    kop = {}
    l = []
    fin = []
    with open("like_info.txt", 'r') as f:
        f = f.read()
        dic = f.split("\n")
        for i in dic:
            i = i.split(":")

            kop[i[0]] = ""
            del i[0]

            l.append(i)

    for i in l:
        w = ":"
        w = w.join(i)
        fin.append(w.lstrip())
    w = 0
    for i in kop:
        kop[i] = fin[w]
        w += 1

    return kop


def head_foll():
    kop = {}
    l = []
    fin = []
    with open("follow_info.txt", 'r') as f:
        f = f.read()
        dic = f.split("\n")
        for i in dic:
            i = i.split(":")

            kop[i[0]] = ""
            del i[0]

            l.append(i)

    for i in l:
        w = ":"
        w = w.join(i)
        fin.append(w.lstrip())
    w = 0
    for i in kop:
        kop[i] = fin[w]
        w += 1

    return kop


with requests.Session() as s:
    if os.path.isfile("cookies.txt"):
        print("1")
        with open("cookies.txt", 'r') as f:
            s.cookies = requests.utils.cookiejar_from_dict(json.load(f))

        jar = requests.cookies.RequestsCookieJar()
        jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
        r = s.get(link, cookies=jar, verify=False)
        sleep(1)
    # print(glob_headers, "\n", b, "\n")
    # glob_headers.update(b)
    # # print("\n\n\n\n", r.headers, type(r.headers))	
    # print("\nZALUPA\n", glob_headers)		
    # r = s.get("https://www.instagram.com/")
    # with open("cookies2.txt", 'wb') as f:
    # 	f.truncate()
    # 	print(r.cookies._cookies)
    # 	pickle.dump(r.cookies._cookies, f)
    # 	#json.dump(requests.utils.dict_from_cookiejar(r.cookies), f)

    # sleep(1)
    # print(jar2)

    else:
        print("2")
        r = s.get(link, verify=False)
        sleep(2)
        csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
        glob_headers["x-csrftoken"] = csrf
        r = s.post(login_url, data=payload, headers=glob_headers, verify=False)

        print(r.status_code, r.cookies)
        with open("cookies.txt", 'w') as f:
            # f.truncate()
            # pickle.dump(r.cookies._cookies, f)
            json.dump(requests.utils.dict_from_cookiejar(r.cookies), f)
    # with open("headers.txt", 'w') as f:
    # 	# f.truncate()
    # 	# pickle.dump(r.cookies._cookies, f)
    # 	json.dump(requests.utils.dict_from_cookiejar(r.headers), f)	

    sleep(1)

    # with open("cookies.txt", 'r') as f:
    # 	# cookies = pickle.load(f)
    # 	# jar2 = requests.cookies.RequestsCookieJar()
    # 	# print(cookies)
    # 	# jar2._cookies = cookies
    # 	# s.cookies = jar2
    # 	s.cookies = requests.utils.cookiejar_from_dict(json.load(f))

    # jar2 = requests.cookies.RequestsCookieJar()
    # jar2.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

    # sleep(2)
    with open("cookies.txt", 'r') as f:
        h = json.load(f)
        d = head_like()

    d["X-CSRFToken"] = h["csrftoken"]

    kuki = d["Cookie"].split(";")
    go = []
    for i in kuki:
        i = i.strip()
        go.append(i)

    est = []
    for i in go:
        i = i.split("=")
        est.append(i)

    print(est, h)
    for i in est:
        if i[0] in h.keys():
            i[1] = h[i[0]]

    print(est)
    fina = ""
    for k in est:
        z = "="
        z = z.join(k)
        z = z + "; "
        print(z)
        fina = fina + z

    fina = fina[:-2]
    print(fina)
    d["Cookie"] = fina
    print(d)

    r = s.post("https://www.instagram.com/web/likes/3447/like/", headers=d, verify=False)
    print(r.cookies)

    # # r = s.get("https://www.instagram.com/baklanskaiav/?__a=1")
    # sleep(1)
    # print(r)
    # with open("cookies_follow.txt", 'r') as f:
    # 	f = f.read()
    # 	dic = dict(item.split('=') for item in f.split(";"))
    # 	print(dic)

    # s.cookies = requests.utils.cookiejar_from_dict(dic)
    # jar2 = requests.cookies.RequestsCookieJar()
    # jar2.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

    # # with open("headers.txt", 'r') as f:
    # # 		# cookies = pickle.load(f)
    # # 		# jar = requests.cookies.RequestsCookieJar()
    # # 		# jar._cookies = cookies
    # # 		# s.cookies = jar
    # # 	s.headers = requests.utils.cookiejar_from_dict(json.load(f))

    # # jarHead = requests.cookies.RequestsCookieJar()
    with open("cookies.txt", 'r') as f:
        h = json.load(f)
        d = head_foll()

    d["X-CSRFToken"] = h["csrftoken"]

    kuki = d["Cookie"].split(";")
    go = []
    for i in kuki:
        i = i.strip()
        go.append(i)

    est = []
    for i in go:
        i = i.split("=")
        est.append(i)

    print(est, h)
    for i in est:
        if i[0] in h.keys():
            i[1] = h[i[0]]

    print(est)
    fina = ""
    for k in est:
        z = "="
        z = z.join(k)
        z = z + "; "
        print(z)
        fina = fina + z

    fina = fina[:-2]
    print(fina)
    d["Cookie"] = fina
    print(d)

    # print("\nHEADERS ", glob_headers, "\n\n")
    # sleep(1) 	
    r = s.post("https://www.instagram.com/web/friendships/39164422021/follow/", headers=d, verify=False)
# print(r)
