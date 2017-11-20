# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas
from ..utils import clear_dict, time_normalize, slug_and_id
from .db_queries import thread_select_by_id, thread_select_by_slug, forum_select_by_id,\
    user_select_by_id

from start import db
from . import error


class ThreadSlugOrIdDetails(ApiHandler):

    def get(self, slug_or_id):
        thread_id = None
        thread_slug = None
        try:
            thread_id = int(slug_or_id)
        except:
            thread_slug = slug_or_id
        # try:
        if thread_id:
            thread = thread_select_by_id.first(thread_id)
        else:
            thread = thread_select_by_slug.first(thread_slug)
        if not thread:
            return error, 404

        thread_id, thread_slug, thread_created_on, thread_message, \
            thread_title, thread_author_id, forum_id \
            = thread

        votes = db.prepare('''SELECT sum(voice) FROM thread 
            JOIN vote ON vote.threadid = thread.id WHERE thread.id = $1''').first(thread_id)
        
        forum_slug = forum_select_by_id.first(forum_id)[1]

        author = user_select_by_id.first(thread_author_id)[1]
        return {'slug': thread_slug, 'forum': forum_slug, 'message': thread_message,
                'title': thread_title, 'author': author, 'id': thread_id,
                'created': time_normalize(thread_created_on), 'votes': votes}, 200
        # except:
        #     import traceback
        #     print(traceback.format_exc())


        # return {'message': 'something', 'title': 'something', 'author': 'something'}, 200, None

    def post(self, slug_or_id):
        # self.json = tornado.escape.json_decode(self.request.body)
        thread_slug, thread_id = slug_and_id(slug_or_id)
        message = self.json.get('message')
        title = self.json.get('title')

        with db.xact():
            thread_update = db.prepare('''UPDATE thread SET message = coalesce($2, message), title = coalesce($3, title) WHERE {cond}
                RETURNING id, slug, created_on, message, title, authorid, forumid'''.format(cond = 'id = $1' if thread_id else 'slug = $1'))

            if thread_id:
                thread = thread_update.first(thread_id, message, title)
            else:
                thread = thread_update.first(thread_slug, message, title)
            
            if not thread:
                return error, 404
            thread_id, thread_slug, thread_created_on, thread_message, \
                thread_title, thread_author_id, forum_id \
                = thread

            author = user_select_by_id.first(thread_author_id)[1]
            forum_slug = forum_select_by_id.first(forum_id)[1]

        return {'slug': thread_slug, 'forum': forum_slug, 'message': thread_message,
                'title': thread_title, 'author': author, 'id': thread_id,
                'created': time_normalize(thread_created_on)}, 200