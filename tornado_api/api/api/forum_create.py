# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from start import db
from . import ApiHandler
from .. import schemas
from . import error

def forum_create(json):
    slug = json['slug']
    title = json['title']
    user = json['user']



class ForumCreate(ApiHandler):

    def post(self):
        slug = self.json['slug']
        title = self.json['title']
        user = self.json['user']
        try:
            with db.xact():
                user_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')
                forum_insert = db.prepare('INSERT INTO forum VALUES (DEFAULT, $1::CITEXT, $2::TEXT, '
                                          '$3::BIGINT)')

                user_record = user_select.first(user)
                if not user_record:
                    return error, 404
                user_id = user_record[0]

                forum_insert(slug, title, user_id)

                return {'slug': slug, 'user': user_record[1], 'title': title}, 201, None
        except:
            forum_select = db.prepare('SELECT * FROM forum WHERE slug = $1::CITEXT')
            forum = forum_select.first(slug)
            print(forum)
            if forum:
                user_select = db.prepare('SELECT * FROM "user" WHERE id = $1::BIGINT')
                user = user_select.first(forum[3])
                username = user[1]
                return {'slug': forum[1], 'user': username, 'title': forum[2]}, 409
