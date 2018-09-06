#!/usr/bin/env python
# encoding: utf-8

import yagmail

#链接邮箱服务器
yag = yagmail.SMTP( user="15651930369@163.com", password="7572896zr", host='smtp.163.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

# 发送邮件
yag.send('1515547772@qq.com', '邮件标题', contents,["D://记事本.txt"])