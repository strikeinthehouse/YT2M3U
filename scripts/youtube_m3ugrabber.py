#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/vijay6672      #
#########################################################################
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://archive.org/download/video-x-ts-1920x-1080-dtd-4/Video%20x%20Ts_1920x1080_dtd-4.ia.mp4')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://archive.org/download/blink182documentary2004/blink182lostdocumentary.ia.mp4')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp


from pytube import YouTube

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Ler os links do arquivo LINKSYOUTUBE.txt
try:
    with open('../youtube_channel_info.txt', 'r') as f:
        links = [line.strip() for line in f.readlines()]
except Exception as e:
    print(f"Erro ao ler o arquivo LINKSYOUTUBE.txt: {e}")
    links = []
        f.write("#EXTM3U\n")
        f.write(banner)
        for i, link in enumerate(links):
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=False)
                if 'url' not in info:
                    print(f"Erro ao gravar informações do vídeo {link}: 'url'")
                    continue
                url = info['url']
                thumbnail_url = info['thumbnail']
                description = info.get('description', '')[:10]
                title = info.get('title', '')
                f.write(f"#EXTINF:-1 group-title=\"YOUTUBE\" tvg-logo=\"{thumbnail_url}\",{title} - {description}...\n")
                f.write(f"{url}\n")
                f.write("\n")
            except Exception as e:
                print(f"Erro ao processar o link {link}: {e}")
                continue
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")    

banner = r'''
#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"
#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"
#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"
#EXTM3U x-tvg-url="https://raw.githubusercontent.com/Nicolas0919/Guia-EPG/master/GuiaEPG.xml"
'''

# Instalando streamlink

subprocess.run(['pip', 'install', 'pytube'])
subprocess.run(['pip', 'install', '--upgrade', 'yt dlp'])

time.sleep(5)
from pytube import YouTube

# Define as opções para o youtube-dl
ydl_opts = {
    'format': 'best',  # Obtém a melhor qualidade

    'write_all_thumbnails': False,  # Não faz download das thumbnails
    'skip_download': True,  # Não faz download do vídeo
}

