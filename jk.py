#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 9:18
# @Author  : zs
# @File    : jk.py

import tornado.ioloop
import tornado.web
import hashlib
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        token = "apitest"
        uid = self.get_argument("uid")
        timestamp = self.get_argument("timestamp")
        rand = self.get_argument("rand")
        param = self.get_argument("param")
        sign = self.get_argument("sign")
        str1 = uid + timestamp + rand + param + token
        domd5 = hashlib.md5(str1.encode('utf8'))
        sign2 = domd5.hexdigest()
        if sign == sign2:
            self.write('验证成功')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

