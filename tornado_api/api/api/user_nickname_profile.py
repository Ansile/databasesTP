# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from start import db
from . import ApiHandler
from .. import schemas
from ..utils import clear_dict
import traceback


error = {
  "message": "Can't find user with id #42\n"
}


class UserNicknameProfile(ApiHandler):

    def get(self, nickname):
        with db.xact():
            user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')
            user = user_select.first(nickname)
        if user:
            return clear_dict({'nickname': user[1], 'about': user[2], 'email':user[3],
                    'fullname': user[4]}), 200
        else:
            return error, 404

    def post(self, nickname):
        about = self.json.get('about')
        email = self.json.get('email')
        fullname = self.json.get('fullname')
        try:
            with db.xact():
                if self.json:
                    user_update = db.prepare('''UPDATE "user" SET about = coalesce($2, about), 
                                             email = coalesce($3, email),
                                             fullname = coalesce($4, fullname) 
                                             WHERE nickname = $1::CITEXT''')
                    affected = user_update.first(nickname, about, email, fullname)
                    if affected is 0:
                       return error, 404
                # elif self.json:
                #     user_update = db.prepare('''UPDATE "user" SET email = $2, fullname = $3
                #                              WHERE nickname = $1::CITEXT''')
                #     affected = user_update.first(nickname, email, None, fullname)
                user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')
                user = user_select.first(nickname)
                if user:
                    about = user[2]
                    email = user[3]
                    fullname = user[4]
                else:
                    return error, 404
            return {'fullname': fullname, 'email': email, 'nickname': nickname, 'about': about}, 200, None
        except Exception as f:
            var = traceback.format_exc()
            print(var)
            return error, 409

