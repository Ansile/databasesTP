# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas
from start import db
from .db_queries import user_select_by_nickname, thread_select_by_slug, thread_select_by_id,\
    forum_select_by_id, user_select_by_id
from . import error
from ..utils import time_normalize

class ThreadSlugOrIdVote(ApiHandler):

    def post(self, slug_or_id):
        print(self.json)
        nickname = self.json['nickname']
        voice = self.json['voice']
        thread_id = None
        thread_slug = None

        try:
            thread_id = int(slug_or_id)
        except:
            thread_slug = slug_or_id

        user = user_select_by_nickname.first(nickname)
        if not user:
            return error, 404
        user_id = user[0]

        if thread_id:
            thread = thread_select_by_id.first(thread_id)
        else:
            thread = thread_select_by_slug.first(thread_slug)
        if not thread:
            return error, 404
        thread_id, thread_slug, thread_created_on, thread_message, \
            thread_title, thread_author_id, forum_id \
            = thread
        forum_slug = forum_select_by_id.first(forum_id)[1]
        # thread_slug = thread[1]
        thread_created_on = time_normalize(thread_created_on)
        # thread_title = thread[3]
        author = user_select_by_id.first(thread_author_id)[1]

        vote_insert = db.prepare('INSERT INTO vote VALUES ($1::INTEGER, $2::BIGINT, $3::BIGINT)'
                                 ' ON CONFLICT ON CONSTRAINT unique_vote DO UPDATE SET voice=$1')
        vote_insert(voice, user_id, thread_id)

        thread_votes_sum_select = db.prepare('SELECT sum(voice) FROM vote WHERE threadid = $1::BIGINT')
        thread_votes_sum = thread_votes_sum_select.first(thread_id)

        return {'message': thread_message, 'title': thread_title, 'author': author,
                'created': thread_created_on, 'id': thread_id, 'slug': thread_slug,
                'votes': thread_votes_sum, 'forum': forum_slug}, 200, None