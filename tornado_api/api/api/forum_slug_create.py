# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ForumSlugCreate(ApiHandler):

    def post(self, slug):
        print(self.json)

        return {'message': 'something', 'title': 'something', 'author': 'something'}, 201, None