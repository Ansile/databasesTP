# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from start import db
from . import ApiHandler
from .. import schemas
from . import error
from ..utils import clear_dict, time_normalize
# import datetime.now
import arrow


class ForumSlugCreate(ApiHandler):

    def post(self, slug):
        author = self.json['author']
        created = self.json.get('created')
        thread_slug = self.json.get('slug')
        message = self.json['message']
        title = self.json['title']
        # try:
        with db.xact():
            if created:
                created = time_normalize(created)

            author_select = db.prepare('SELECT * FROM "user" WHERE nickname = $1::CITEXT')
            forum_select = db.prepare('SELECT * FROM forum WHERE slug = $1::CITEXT')
            thread_create = db.prepare('INSERT INTO thread VALUES (DEFAULT, $1::CITEXT, $2::TEXT::TIMESTAMP, '
                                      '$3::TEXT, $4::TEXT, $5::BIGINT, $6::BIGINT) RETURNING id')
            forum = forum_select.first(slug)
            author = author_select.first(author)
            thread_id = thread_create.first(thread_slug, created, message, title, author[0], forum[0])
            # Debug
            # thread_select = db.prepare('SELECT * FROM thread WHERE id = $1::BIGINT')
            # thread = thread_select.first(thread_id)
            # print(thread[2])
            # print(type(thread[2]))
            # created = arrow.Arrow.fromdatetime(thread[2])
            # created = created.for_json()
            # print(created)
            #Debug

            return clear_dict({'slug': thread_slug, 'forum': forum[1], 'message': message, 'title': title, 'author': author[1], 'id': thread_id, 'created': created}), 201, None
