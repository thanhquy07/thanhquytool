from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
edit = vang+"]"+trang+"["+do+"[⟨⟩]"+trang+"]"+vang+"["+trang+" ➩ "+luc
edit1 = trang+"["+do+"[⟨⟩]"+trang+"]"+trang+" ➩ "+luc
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;34m╔═════════════════════════════════════════════════════════════════╗
\033[1;32m║ ████████╗ ███████╚╗       ████████╗ █████╗  █████╗ ██╗          ║
\033[1;35m║ ╚══██╔══╝██║   ██║        ╚══██╔══╝██╔══██╗██╔══██╗██║          ║
\033[1;31m║    ██║   ██║   ██║   █████╗  ██║   ██║  ██║██║  ██║██║          ║
\033[1;33m║    ██║   ██║ ████╚╗  ╚════╝  ██║   ██║  ██║██║  ██║██║          ║
\033[1;34m║    ██║   ╚█████████║         ██║   ╚█████╔╝╚█████╔╝██████╗      ║
\033[1;37m║    ╚═╝    ╚════╗██║          ╚═╝    ╚════╝  ╚════╝ ╚═════╝      ║
\033[1;37m║                ╚══╝                                             ║
\033[1;34m╠═════════════════════════════════════════════════════════════════╣
\033[1;32m║➢ Admin    : Thành Quý Tool                                      ║
\033[1;36m║➢ Youtube  : https://youtube.com/@thanhquytool                   ║
\033[1;31m║➣ Zalo     : 0355879036                                          ║
\033[1;34m╚═════════════════════════════════════════════════════════════════╝
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print(f"{trang} ➩ Ngày{trang} : {do}{ngay_hom_nay}{vang} |{luc} Tháng{trang}: {do}{thang_nay} {vang}| {luc}Năm{trang}: {do}{nam_}{vang} | {luc}Thời Gian: {do}{time}")
print(f'{trang} ➩ IP Hiện Tại Của Bạn : {vang}{ip}')
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Golike        \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Golike Tik Tok")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool Golike Twittet/X")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool Golike Instagram")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/thanhquy07/thanhquytool/main/golike/TQToolTikTok.py').text)
if chon == 2 :
	exec(requests.get('https://raw.githubusercontent.com/thanhquy07/thanhquytool/main/golike/TQToolTwitter.py').text)
if chon == 3 :
	exec(requests.get('https://raw.githubusercontent.com/thanhquy07/thanhquytool/main/golike/TQToolIntagram.py').text)
else :
	print (" Sai Lựa Chọn ")
	exit()