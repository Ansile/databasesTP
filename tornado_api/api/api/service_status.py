# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from .db_queries import db
from . import ApiHandler
from .. import schemas


class ServiceStatus(ApiHandler):

    def get(self):
        status = db.prepare('''
            SELECT count(forum.id) FROM forum
            UNION ALL
            SELECT count(thread.id) FROM thread
            UNION ALL
            SELECT count("user".id) FROM "user"
            UNION ALL
            SELECT count(message.id) FROM message''')()

        return {'forum': status[0][0], 'post': status[3][0], 'thread': status[1][0], 'user': status[2][0]},\
            200, None