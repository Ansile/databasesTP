# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ForumSlugUsers(ApiHandler):

    def get(self, slug):
        print(self.args)

        return [], 200, None