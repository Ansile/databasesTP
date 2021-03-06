# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas
from .db_queries import db
from ..utils import clear_dict
import tornado.escape
from postgresql import exceptions

Debug = False


class UserNicknameCreate(ApiHandler):
    def post(self, nickname):
        about = self.json.get('about')
        email = self.json.get('email')
        fullname = self.json.get('fullname')
        try:
            with db.xact():
                user_insert = db.prepare('INSERT INTO "user" VALUES (DEFAULT, $1::citext, $2::citext, $3::citext, '
                                         '$4::citext)')
                user_insert(nickname, about, email, fullname)
        except exceptions.UniqueError:
            if Debug:
                print('email' + email)
            user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::citext OR email = $2::citext')
            conflict_list = []
            for _, ex_nickname, ex_about, ex_email, ex_fullname in user_select(nickname, email):
                if Debug:
                    print({'nickname': ex_nickname, 'about': ex_about, 'email': ex_email,
                     'fullname': ex_fullname})
                conflict_list.append(clear_dict({'nickname': ex_nickname, 'about': ex_about, 'email': ex_email,
                                                 'fullname': ex_fullname}))
            if Debug:
                print(conflict_list)
            return conflict_list, 409, None
        return clear_dict({'nickname': nickname, 'about': about, 'email': email,
                'fullname': fullname}), 201, None