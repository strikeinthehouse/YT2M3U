#!/usr/bin/python3

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

def is_channel_live(url):
    response = requests.get(url, timeout=15)
    return response.status_code == 200

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        if windows:
            return 'https://archive.org/download/video-x-ts-1920x-1080-dtd-4/Video%20x%20Ts_1920x1080_dtd-4.ia.mp4'
        os.system(f'wget {url} -O temp.txt')
        response = ''.join(open('temp.txt').readlines())
        if '.m3u8' not in response:
            return 'https://archive.org/download/blink182documentary2004/blink182lostdocumentary.ia.mp4'
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
    return link[start : end]

output_file = 'output.m3u'  # Nome do arquivo de saída

with open('../youtube_channel_info.txt', errors="ignore") as f:
    with open(output_file, 'w') as output:
        output.write('#EXTM3U x-tvg-url="https://github.com/botallen/epg/releases/download/latest/epg.xml"\n')
        output.write(banner)
        
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
                channel_url = line[4].strip()  # Assuming the channel URL is in the 5th position in the line
                if is_channel_live(channel_url):
                    output.write(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}\n')
                    output.write(grab(channel_url) + '\n')
            else:
                output.write(grab(line) + '\n')

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
