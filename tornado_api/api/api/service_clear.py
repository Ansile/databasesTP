# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from start import db
from . import ApiHandler
from .. import schemas


class ServiceClear(ApiHandler):

    def post(self):
        clear = db.execute('TRUNCATE "user", message, thread, forum, vote CASCADE;')

        return None, 200, None