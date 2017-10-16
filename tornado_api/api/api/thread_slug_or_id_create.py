# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import tornado.escape
from . import ApiHandler
from .. import schemas


class ThreadSlugOrIdCreate(ApiHandler):
    # def initialize(self):
    #     pass
    #     # self.json = tornado.escape.json_decode(self.request.body)

    def post(self, slug_or_id):
        self.json = tornado.escape.json_decode(self.request.body)
        print(self.json)


        return [], 201, None