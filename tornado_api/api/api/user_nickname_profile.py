# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
# from ... import db
from . import ApiHandler
from .. import schemas


class UserNicknameProfile(ApiHandler):

    def get(self, nickname):

        return {'fullname': 'something', 'email': 'something'}, 200, None

    def post(self, nickname):
        print(self.json)

        return {'fullname': 'something', 'email': 'something'}, 200, None