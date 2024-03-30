import requests
import os
import json
import time

headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin': 'https://bible.prsi.org/zh-hans/Player',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
        }
payload = {}

def download():    
    album_name = '圣经-华语有声戏剧圣经'    
    dir = 'media/{}'.format(album_name)
    if not os.path.exists(dir):
        os.mkdir(dir)
        print("不存在目录，已创建:{}".format(album_name))

    for book in range(1,67):
        chapter = 0
        while True:  
            chapter = chapter+1
            media_file_path = os.path.join(dir, '{}-{}.mp3'.format(str(book).zfill(2),  str(chapter).zfill(3)))
            if os.path.exists(media_file_path): # 已经保存过的跳过
                continue
                
            url = 'https://bible.prsi.org/zh-hant/Player/getaudiomedia?book={}&chapter={}'.format(book, chapter) 
            info_response = requests.request("GET", url, headers=headers, data=payload)

            # 章超过了会500, 则中断进入下一卷
            if info_response.status_code == 500:
                if info_response.text.find('Index was out of range'):                    
                    print("换卷,{},{}".format(book, chapter-1))
                    break
            
            # 出了错则暂停3秒继续下一下章
            if info_response.status_code != 200:
                print("info_error,{}-{}".format(book, chapter))
                time.sleep(3000)               
                continue

            info = json.loads(info_response.text)            
            mp3_response = requests.request("GET", info['mp3'], headers=headers, data=payload)
            # 出了错则暂停3秒继续下一下章
            if mp3_response.status_code != 200:
                print("mp3_erro,{},{}".format(book, chapter))
                time.sleep(3000)               
                continue

            with open(media_file_path,'wb') as f: 
                f.write(mp3_response.content)
            
            print('success,{},{}'.format(book, chapter))


if __name__ == '__main__': 
    download()