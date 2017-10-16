# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas
from ..utils import clear_dict, time_normalize


class ThreadSlugOrIdDetails(ApiHandler):

    def get(self, slug_or_id):
        return clear_dict({'slug': thread_slug, 'forum': forum[1], 'message': message, 'title': title,
                           'author': author[1], 'id': thread_id, 'created': created}), 201, None
        return {'message': 'something', 'title': 'something', 'author': 'something'}, 200, None

    def post(self, slug_or_id):
        print(self.json)

        return {'message': 'something', 'title': 'something', 'author': 'something'}, 200, None