# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class PostIdDetails(ApiHandler):

    def get(self, id):
        print(self.args)

        return {}, 200, None

    def post(self, id):
        print(self.json)

        return {'message': 'something', 'author': 'something'}, 200, None