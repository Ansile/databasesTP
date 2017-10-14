# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ThreadSlugOrIdPosts(ApiHandler):

    def get(self, slug_or_id):
        print(self.args)

        return [], 200, None