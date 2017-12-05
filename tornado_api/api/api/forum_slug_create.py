# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from .db_queries import db
from . import ApiHandler
from .. import schemas
from . import error
from ..utils import clear_dict, time_normalize
# import datetime.now
from postgresql import exceptions
import arrow


class ForumSlugCreate(ApiHandler):

    def post(self, slug):
        author = self.json['author']
        created = self.json.get('created')
        thread_slug = self.json.get('slug')
        message = self.json['message']
        title = self.json['title']
        try:
            with db.xact():
                if created:
                    db_created = time_normalize(created)
                    created = time_normalize(created, for_json=True)
                else:
                    db_created = None

                author_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')
                forum_select = db.prepare('SELECT * FROM forum WHERE slug = $1::CITEXT')
                thread_create = db.prepare('INSERT INTO thread VALUES (DEFAULT, $1::CITEXT, $2::TEXT::TIMESTAMP, '
                                          '$3::TEXT, $4::TEXT, $5::BIGINT, $6::BIGINT) RETURNING id')
                forum = forum_select.first(slug)
                if not forum:
                    return error, 404
                author = author_select.first(author)
                if not author:
                    return error, 404
                thread_id = thread_create.first(thread_slug, db_created, message, title, author[0], forum[0])
                # Debug
                # thread_select = db.prepare('SELECT * FROM thread WHERE id = $1::BIGINT')
                # thread = thread_select.first(thread_id)
                # print(thread[2])
                # print(type(thread[2]))
                # created = arrow.Arrow.fromdatetime(thread[2])
                # created = created.for_json()
                # print(created)
                #Debug

                return clear_dict({'slug': thread_slug, 'forum': forum[1], 'message': message, 'title': title,
                                   'author': author[1], 'id': thread_id, 'created': created}), 201, None
        except exceptions.UniqueError:
            thread_select = db.prepare('SELECT * FROM thread WHERE slug = $1::CITEXT')
            thread = thread_select.first(thread_slug)
            thread_id = thread[0]
            forum_id = thread[6]
            author_id = thread[5]
            author = db.prepare('SELECT * FROM "user" WHERE id = $1::BIGINT').first(author_id)
            forum = db.prepare('SELECT * FROM forum WHERE id = $1::BIGINT').first(forum_id)

            return clear_dict({'slug': thread[1], 'forum': forum[1], 'message': thread[3], 'title': thread[4],
                               'author': author[1], 'id': thread_id, 'created': time_normalize(thread[2], for_json=True)}), 409
