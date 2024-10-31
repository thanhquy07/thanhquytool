import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep  # Đã sửa lỗi ở đây
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

def bes4(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            version_tag = soup.find('span', id='version_vip')
            maintenance_tag = soup.find('span', id='maintenance_vip')
            version = version_tag.text.strip() if version_tag else None
            maintenance = maintenance_tag.text.strip() if maintenance_tag else None
            return version, maintenance
    except requests.RequestException:
        return None, None
    return None, None

def checkver():
    url = 'https://checkserver.hotrommo.com/'
    version, maintenance = bes4(url)
    if maintenance == 'on':
        print("\033[1;31mTool đang được bảo trì. Vui lòng thử lại sau. \nHoặc vào nhóm Tele: \033[1;33mhttps://t.me/+77MuosyD-yk4MGY1")
        sys.exit()
    return version

current_version = checkver()
if current_version:
    print(f"Phiên bản hiện tại: {current_version}")
else:
    print("Không thể lấy thông tin phiên bản hoặc tool đang được bảo trì.")
    sys.exit()

def banner():
 os.system("cls" if os.name == "nt" else "clear")
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
  sleep(0.000001)
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()  # Trả về từ điển JSON
        ip_address = ip_data['ip']  # Lấy giá trị từ trường 'ip'
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

# Hàm để hiển thị địa chỉ IP của thiết bị
def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'thanhquytool{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://thanhquy07.github.io/website/?key={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link(link_key_yeumoney):
    try:
        response = requests.get(f'https://yeumoney.com/QL_api.php?token=4217ac40210a03869989f118de9a1b99f9f026987e3f4204dc28fe612bfe2074&format=json&url={link_key_yeumoney}')
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return None
def get_shortened_link_phu(url):
    token_yeumoney = '4217ac40210a03869989f118de9a1b99f9f026987e3f4204dc28fe612bfe2074'
    try:
        yeumoney_response = requests.get(f'https://yeumoney.com/QL_api.php?token={token_yeumoney}&format=json&url={url}')
        if yeumoney_response.status_code == 200:
            return yeumoney_response.json()
    except requests.RequestException:
        return None
def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;35mTool còn hạn, mời bạn dùng tool.")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 1 Để Lấy Key \033[1;33m( Free )")
                while True:
                    try:
                        try:
                            choice = input("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;34mChọn lựa chọn: ")
                            print("\033[97m════════════════════════════════════════════════")
                        except KeyboardInterrupt:
                            print("\n\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mCảm ơn bạn đã dùng Tool Thành Quý Tool. Thoát...")
                            sys.exit()
                        
                        if choice == "1":  # Kiểm tra chuỗi "1"
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                token_link4m = '664efe0fe5762652e171afca'
                                link4m_response = requests.get(f'https://link4m.co/api-shorten/v2?api={token_link4m}&format=json&url={link_key_yeumoney}', timeout=5)
                                print("\033[1;31mLưu Ý: \033[1;33mTool Free Nhé Cả Nhà Yêu \033[1;91m❣\033[1;32m")
                                
                                if link4m_response.status_code == 200:
                                    link4m_data = link4m_response.json()
                                    if link4m_data.get('status') == "error":
                                        print(link4m_data.get('message'))
                                        return
                                    else:
                                        link_key_4m = link4m_data.get('shortenedUrl')
                                        print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mLink Để Vượt Key Là:', link_key_4m)
                                else:
                                    print('Không thể kết nối đến dịch vụ rút gọn URL')
                                    return
                        
                            while True:
                                keynhap = input('Key Đã Vượt Là: ')
                                if keynhap == key:
                                    print('Key Đúng Mời Bạn Dùng Tool')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return  # Thoát khỏi vòng lặp và hàm main
                                else:
                                    print('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mKey Sai Vui Lòng Vượt Lại Link:', link_key_4m)
                                            # Nếu người dùng nhập không phải 1 hoặc 2, yêu cầu nhập lại
                            banner()
                            print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;91m✈  Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                            print("\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNhập 1 Để Lấy Key \033[1;33m( Free )")
                            continue  # Quay lại đầu vòng lặp
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")

        if da_qua_gio_moi():
            print("Key của bạn đã hết hạn. Đợi 2 giây để lấy key mới từ ngày mới...")
            time.sleep(2)
            main()  # Gọi lại main() để lấy key mới từ ngày mới
    else:
        print("Không thể lấy địa chỉ IP.")

if __name__ == '__main__':
    main()

while True:
    try:
        exec(requests.get('https://raw.githubusercontent.com/thanhquy07/thanhquytool/main/index.py').text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mCảm ơn bạn đã dùng Tool Thành Quý Tool. Thoát...")
        sys.exit()