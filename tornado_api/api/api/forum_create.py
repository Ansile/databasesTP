# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ForumCreate(ApiHandler):

    def post(self):
        print(self.json)

        return {'slug': 'something', 'user': 'something', 'title': 'something'}, 201, None