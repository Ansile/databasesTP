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
                user_insert = db.prepare('INSERT INTO "user" VALUES (DEFAULT, $1::citext, $2::citext, $3::citext, '
                                         '$4::citext)')
                user_insert(nickname, about, email, fullname)
        except:
            print('email' + email)
            user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::citext OR email = $2::citext')
            conflict_list = []
            for _, ex_nickname, ex_about, ex_email, ex_fullname in user_select(nickname, email):
                print({'nickname': ex_nickname, 'about': ex_about, 'email': ex_email,
                 'fullname': ex_fullname})
                conflict_list.append(clear_dict({'nickname': ex_nickname, 'about': ex_about, 'email': ex_email,
                                                 'fullname': ex_fullname}))
            print(conflict_list)
            return conflict_list, 409, None
        return clear_dict({'nickname': nickname, 'about': about, 'email': email,
                'fullname': fullname}), 201, None