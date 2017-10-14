# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from start import db
from . import ApiHandler
from .. import schemas
from ..utils import clear_dict

error = {
  "message": "Can't find user with id #42\n"
}


class UserNicknameProfile(ApiHandler):

    def get(self, nickname):
        with db.xact():
            user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')
            user = user_select.first(nickname)
        print(user)
        return clear_dict({'nickname': user[1], 'about': user[2], 'email':user[3],
                'fullname': user[4]}), 200

    def post(self, nickname):
        # print(self.json)
        about = self.json.get('about')
        email = self.json.get('email')
        fullname = self.json.get('fullname')
        try:
            with db.xact():
                if about is not None:
                    user_select = db.prepare('''UPDATE "user" SET about = $2, email = $3, fullname = $4 
                                             WHERE nickname = $1::CITEXT''')
                    affected = user_select.first(nickname, about, email, fullname)
                else:
                    user_select = db.prepare('''UPDATE "user" SET email = $2, fullname = $3 
                                             WHERE nickname = $1::CITEXT''')
                    affected = user_select.first(nickname, email, fullname)

                if affected == 0:
                   return error, 404
                print('affected= ' + str(affected))

            return {'fullname': fullname, 'email': email, 'nickname': nickname, 'about': about}, 200, None
        except:
            return error, 409

