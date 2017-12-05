# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import tornado.escape
from . import ApiHandler
from .. import schemas
from .db_queries import db
from . import error
import arrow
import re
from ..utils import time_normalize, int_convert
from postgresql.types import Array


Debug = False

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

        created = time_normalize(arrow.Arrow.utcnow())
        # created_json = time_normalize(created, for_json=True)
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
                if not self.json:
                    return [], 201

                thread_id = thread[0]
                message_parents_select = db.prepare('SELECT threadid FROM message WHERE id = ANY ($1)')
                author_select = db.prepare('SELECT * FROM "user" WHERE nickname = ANY($1)')

                message_insert = db.prepare('INSERT INTO message VALUES (DEFAULT, $1::TEXT::TIMESTAMP, $2::TEXT, FALSE,'
                                            ' $3::BIGINT, $4::BIGINT, $5::BIGINT, $6::BIGINT, $7::BIGINT[] || $8::BIGINT)')

                forum_select = db.prepare('SELECT * FROM forum WHERE id = $1::BIGINT')
                forum = forum_select.first(thread[6])
                forum_slug = forum[1]
                forum_id = forum[0]

                message_parents = set()
                for item in self.json:
                    authors.append(item['author'])
                    parent = item.get('parent')
                    if parent:
                        message_parents.add(parent)

                message_parent_thread_ids = message_parents_select(list(message_parents))
                if len(message_parent_thread_ids) < len(message_parents):
                    # print(message_parent_thread_ids, message_parents)
                    return error, 409 #fake parent

                for parent_thread_id in message_parent_thread_ids:
                    if parent_thread_id[0] != thread_id:
                        # print(message_parent_thread_ids) 
                        return error, 409 #parent from different thred

                author_records = author_select(authors) 

                nickname_to_id = {}
                id_to_nickname = {}
                for author_id, author_nickname, _, _, _ in author_records:
                    nickname_to_id[author_nickname] = author_id
                    id_to_nickname[author_id] = author_nickname

                messages = []
                message_parent_select = db.prepare('SELECT parenttree FROM message where message.id = $1::BIGINT')

                try:
                    for item in self.json:
                        parent_id = item.get('parent', None)
                        message_parent = None
                        if parent_id:
                            message_parent = message_parent_select.first(parent_id)
                            messages.append((created, item['message'], nickname_to_id[item['author']], item.get('parent', None),
                                        thread_id, forum_id, message_parent, parent_id))
                        else:
                            messages.append((created, item['message'], nickname_to_id[item['author']], item.get('parent', None),
                                        thread_id, forum_id, Array([]), 0))
                except KeyError:
                    return error, 404

                message_insert.load_rows(messages)
                last_id_select = db.prepare('select CURRVAL(\'message_id_seq\')')
                last_id = last_id_select.first()
                if Debug:
                    print('author_records')
                    print(author_records)
                    print(last_id)
                    print(created)
                    print(type(created))
                    
                created_json = time_normalize(created, for_json=True)
                if Debug:
                    print('created')
                    print(created)
                    print(len(created))
                    print(repr(created))
                    print(type(created))
                result = []
                message_count = len(messages)
                for counter in range(message_count):
                    x = messages[counter]
                    message = {'created': created_json, 'message': x[1], 'author': id_to_nickname[x[2]],
                               'id': last_id - message_count + counter + 1, 'parent': int_convert(x[3]),
                               'thread': thread_id, 'forum': forum_slug}
                    if Debug:
                        print(message)
                    result.append(message)
                    counter += 1

                return result, 201
        except:
            import traceback
            print(traceback.format_exc())


        # return [], 201, None