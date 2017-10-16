# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import tornado.escape
from . import ApiHandler
from .. import schemas
from start import db
from . import error
import arrow

class ThreadSlugOrIdCreate(ApiHandler):
    # def initialize(self):
    #     pass
    #     # self.json = tornado.escape.json_decode(self.request.body)

    def post(self, slug_or_id):
        self.json = tornado.escape.json_decode(self.request.body)
        thread_id = None
        try:
            thread_id = int(slug_or_id)
        except:
            slug = slug_or_id
            # print(self.json)
        authors = []
        if not self.json:
            return [], 201
        created = arrow.Arrow.utcnow().isoformat(sep=' ')
            # created = self.json[0]['created']
        # for item in self.json:
        #     authors.append(item['author'])
        try:
                with db.xact():
                    if thread_id is not None:
                        thread_select = db.prepare('SELECT * FROM thread WHERE id = $1::BIGINT')
                        thread = thread_select.first(thread_id)
                    else:
                        thread_select = db.prepare('SELECT * FROM thread WHERE slug = $1::CITEXT')
                        thread = thread_select.first(slug)
                    if not thread:
                        return error, 404
                thread_id = thread[0]
                author_select = db.prepare('SELECT * FROM "user" WHERE nickname = ANY($1)')
                message_insert = db.prepare('INSERT INTO message VALUES (DEFAULT, $1::TEXT::TIMESTAMP, $2::TEXT, FALSE,'
                                            ' $3::BIGINT, $4::BIGINT, $5::BIGINT, $6::BIGINT) RETURNING id')

                forum_select = db.prepare('SELECT * FROM forum WHERE id = $1::BIGINT')
                forum = forum_select.first(thread[6])
                forum_slug = forum[1]
                forum_id = forum[0]
                for item in self.json:
                    authors.append(item['author'])
                author_records = author_select(authors)

                nickname_to_id = {}
                id_to_nickname = {}
                for author_id, author_nickname, _, _, _ in author_records:
                    nickname_to_id[author_nickname] = author_id
                    id_to_nickname[author_id] = author_nickname

                messages = []
                for item in self.json:
                    messages.append((created, item['message'], nickname_to_id[item['author']], item.get('parent', 0),
                                    thread_id, forum_id))
                message_insert.load_rows(messages)
                last_id_select = db.prepare('select CURRVAL(\'message_id_seq\')')
                last_id = last_id_select.first()
                print('author_records')
                print(author_records)
                print(last_id)
                created = arrow.get(created).isoformat()
                result = []
                message_count = len(messages)
                for counter in range(message_count):
                    x = messages[counter]
                    result.append({'created': created, 'message': x[1], 'author': id_to_nickname[x[2]],
                                   'id': last_id - message_count + counter + 1, 'parent': x[3],
                                   'thread': thread_id, 'forum': forum_slug})
                    counter += 1

                return result, 201
        except:
            import traceback
            print(traceback.format_exc())


        return [], 201, None