#! /usr/bin/python3

banner = r'''
#########################################################################
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

with open('../youtube_channel_info.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}\n', end='')
        else:
            grab(line)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')

