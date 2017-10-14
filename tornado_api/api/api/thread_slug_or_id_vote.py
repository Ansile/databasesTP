# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ThreadSlugOrIdVote(ApiHandler):

    def post(self, slug_or_id):
        print(self.json)

        return {'message': 'something', 'title': 'something', 'author': 'something'}, 200, None