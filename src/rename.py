import os

def rename():
   contents = get_bible_contents()
   base_dir = 'media/圣经-华语有声戏剧圣经/'

   for file_name in  os.listdir(base_dir):
      if not file_name.endswith('.mp3'):
        continue     
      index = int(file_name.split('-')[0]) # 从1开始
      new_name = '{}-{}-{}'.format(str(index).zfill(2), contents[index-1], file_name.split('-')[1]) # 从1开始
      print(file_name + " " + new_name)
      os.rename(base_dir + file_name, base_dir + new_name)

def get_bible_contents():
   return [
    '创世记',
    '出埃及记',
    '利未记',
    '民数记',
    '申命记',
    '约书亚记',
    '士师记',
    '路得记',
    '撒母耳记上',
    '撒母耳记下',
    '列王记上',
    '列王记下',
    '历代志上',
    '历代志下',
    '以斯拉记',
    '尼希米记',
    '以斯帖记',
    '约伯记',
    '诗篇',
    '箴言',
    '传道书',
    '雅歌',
    '以赛亚书',
    '耶利米书',
    '耶利米哀歌',
    '以西结书',
    '但以理书',
    '何西阿书',
    '约珥书',
    '阿摩司书',
    '俄巴底亚书',
    '约拿书',
    '弥迦书',
    '那鸿书',
    '哈巴谷书',
    '西番雅书',
    '哈该书',
    '撒迦利亚书',
    '玛拉基书',
    '马太福音',
    '马可福音',
    '路加福音',
    '约翰福音',
    '使徒行传',
    '罗马书',
    '哥林多前书',
    '哥林多后书',
    '加拉太书',
    '以弗所书',
    '腓立比书',
    '歌罗西书',
    '帖撒罗尼迦前书',
    '帖撒罗尼迦后书',
    '提摩太前书',
    '提摩太后书',
    '提多书',
    '腓利门书',
    '希伯来书',
    '雅各书',
    '彼得前书',
    '彼得后书',
    '约翰壹书',
    '约翰贰书',
    '约翰叁书',
    '犹大书',
    '启示录',
    ]


if __name__ == '__main__':
   rename()