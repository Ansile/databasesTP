# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas
from start import db
from ..utils import clear_dict


class UserNicknameCreate(ApiHandler):

    def post(self, nickname):
        about = self.json.get('about')
        email = self.json.get('email')
        fullname = self.json.get('fullname')
        try:
            with db.xact():
                user_insert = db.prepare('INSERT INTO "user" VALUES (DEFAULT, $1::text, $2::text, $3::text, $4::text)')
                user_insert(nickname, about, email, fullname)
        except:
            user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::text OR email = $2::text')
            conflict_list = []
            for _, ex_nickname, ex_about, ex_email, ex_fullname in user_select(nickname, email):
                conflict_list.append(clear_dict({'nickname': ex_nickname, 'about': ex_about, 'email': ex_email,
                                                 'fullname': ex_fullname}))
            return conflict_list, 409, None
        return clear_dict({'nickname': nickname, 'about': about, 'email': email,
                'fullname': fullname}), 201, None