# 华语圣经戏剧版下载

提供网页版播放 [戏剧圣经](https://bible.prsi.org/zh-hans/Player)

素材:
1. 循环圣经卷和章获取音频信息
https://bible.prsi.org/zh-hant/Player/getaudiomedia?book=1&chapter=1
    - book为卷
    - chapter为章

2. 返回的json
josn对象的mp3字段为音频下载地址
```
{"mp3":"https://d16muzjy2nvk7e.cloudfront.net/BibleContent/CADB/Audio/EQ/cadb_01001.mp3?Expires=1711772733\u0026Signature=lJmjFhlFU7RhUlLI~i2KKo4DxpB1hLIPQZ5m4-LLUH5p1fQY6JYpLsUsPCB9OSPpCaKYg-HqMGgRBtzsSxW7B8OlcB-v28Q3uonUvxPQkXu3vsBfm9BgSoTxCHEyk6Kz09E7EkZzGAPcV4kS4q7-M0-B94q8My4CHtmqeZwpUGjvpWo2rkUp1Q0Qih-KrFxVaJ9dqoTuw6sbR~r~j1Sr-mER6lZrkwuYhB4KXtdbSjibbRapafrAIftavXQxWk-tnX9eQYv9t5~zr2ssRSb0QlWkelrd0kZlyihLD0~XLPahL0rh9gMdTZvGZhFHn8uj6iG7yAyGR2QrNfExR-paiw__\u0026Key-Pair-Id=APKAIIV6ED7L6A432UGA"}
```

5. 实现方式
循环卷和章，不用管有多少，返回404即可继续下一卷和章
