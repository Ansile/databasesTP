# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ForumSlugDetails(ApiHandler):

    def get(self, slug):

        return {'slug': 'something', 'user': 'something', 'title': 'something'}, 200, None