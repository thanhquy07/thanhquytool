import requests
import os
from datetime import datetime
import concurrent.futures
from colorama import init, Fore
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
import requests
import socket
import os, sys
trang = "\033[1;37m"
luc = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lam = "\033[1;36m"
System.Title("GEN Proxy")
print("""
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
""")
def get_static_api_content(api_urls):
    api_content = []
    for api_url in api_urls:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.text.split("\n")
            api_content.extend(data)
            print(f"{Fore.GREEN}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Scan Proxy từ API -> https://apiv1.dagtri.org/proxy/maybiluaroi{Fore.RESET}")
        else:
            print(f"{Fore.RED}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Failed Scan Proxy từ API -> https://apiv1.dagtri.org/proxy/maybiluaroi{Fore.RESET}")
    return api_content

def download_files_from_api(api_urls, output_directory):
    proxy_list = []

    # Fetch content from static APIs
    static_api_content = get_static_api_content(api_urls)

    for content in static_api_content:
        proxies = content.split("\n")
        proxy_list.extend(proxies)

    # Fetch content from download APIs
    for api_url in api_urls_download:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.text.split("\n")
            proxy_list.extend(data)
            print(f"{Fore.GREEN}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Scan Proxy từ API -> https://apiv1.dagtri.org/proxy/maybiluaroi{Fore.RESET}")
        else:
            print(f"{Fore.RED}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Failed Scan Proxy từ API -> https://apiv1.dagtri.org/proxy/maybiluaroi{Fore.RESET}")

    # Save all proxies into individual files named by date
    if proxy_list:
        date_string = datetime.today().strftime('%Y-%m-%d')
        file_name = f"proxies_{date_string}.txt"
        output_path = os.path.join(output_directory, file_name)
        with open(output_path, 'w') as f:
            for proxy in proxy_list:
                proxy = proxy.strip()  # Remove leading and trailing spaces
                f.write(proxy + "\n")
        print(f"{Fore.GREEN}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Đã lưu file proxy thành công{Fore.RESET}")
    else:
        print(f"{Fore.RED}\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Không có proxy nào trong file cả{Fore.RESET}")

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama
    api_urls_download = [
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&ssl=yes',
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    ]
    api_urls_static = [
        'https://www.proxy-list.download/api/v1/get?type=http&anon=elite',
        'https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous',
    ]
    all_api_urls = api_urls_download + api_urls_static
    output_directory = os.getcwd()  # Current working directory

    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Step 1: Download files from the APIs and save with date-based filenames
    download_files_from_api(all_api_urls, output_directory)
