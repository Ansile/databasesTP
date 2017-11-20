# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from start import db
from . import error
from . import ApiHandler
from ..utils import clear_dict, time_normalize
from .. import schemas


class PostIdDetails(ApiHandler):

    def get(self, id):
        id = int(id)
        related = self.get_arguments('related')
        print(related)

        related_items = { 'user': False, 'thread': False, 'forum': False }

        if (related):
            related = related[0].split(',')
        for item in related:
            if item in ['user', 'thread', 'forum']:
                related_items[item] = True
                print(item)

        message_fields_len = 6

        #Get everything in one sweep motion
        message_select = db.prepare('''
            SELECT m.created_on, m.message, "user".nickname, m.threadid, forum.slug, isedited 
            {thread_fields}
            {forum_fields}
            {user_fields}
            FROM
            (SELECT authorid, threadid, forumid, parentid, created_on, message, isedited FROM message
            WHERE id = $1) as m
            JOIN "user" ON "user".id = m.authorid
            JOIN forum ON m.forumid = forum.id
            {join_thread}
            {join_forum_author}'''.format(
                join_thread = 'JOIN thread on m.threadid = thread.id '
                'JOIN "user" AS thread_author ON thread_author.id = thread.authorid' if related_items['thread'] else '',
                thread_fields = ', thread.id, thread.slug, thread.created_on, '
                    'thread.message, thread.title, thread_author.nickname' if related_items['thread'] else '',
                join_forum_author = 'JOIN "user" AS forum_author ON forum_author.id = forum.userid' if related_items['forum'] else '',
                forum_fields = ', forum.id, forum.title, forum_author.nickname' if related_items['forum'] else '',
                user_fields = ', "user".about, "user".email, "user".fullname' if related_items['user'] else ''))

        message = message_select.first(id)
        if not message:
            return error, 404

        if related_items['thread']:
            thread_offset = message_fields_len
            thread = { 'id': message[thread_offset], 'slug': message[thread_offset + 1], 
                'created': time_normalize(message[thread_offset + 2]), 'message': message[thread_offset + 3], 
                'title': message[thread_offset + 4], 'author': message[thread_offset + 5],
                'forum': message[4] }
            thread_fields_len = 6
        else: 
            thread = None
            thread_fields_len = 0

        if related_items['forum']:
            forum_offset = message_fields_len + thread_fields_len
            forum_fields_len = 3
            forum = { 'id' : message[forum_offset], 'slug': message[4], 
                'title': message[forum_offset + 1], 'user': message[forum_offset + 2]} 
            #Optimization zone
            forum['posts'] = db.prepare('SELECT COUNT(id) FROM message WHERE forumid = $1').first(forum['id'])
            forum['threads'] = db.prepare('SELECT COUNT(id) FROM thread WHERE forumid = $1').first(forum['id']) 
        else:
            forum = None
            forum_fields_len = 0


        if related_items['user']:
            user_offset = message_fields_len + forum_fields_len + thread_fields_len
            user = { 'nickname': message[2], 'about': message[user_offset], 
                'email': message[user_offset + 1], 'fullname': message[user_offset + 2] }
        else:
            user = None

        post = { 'id': id, 'created': time_normalize(message[0]), 'message': message[1], 'author': message[2],
            'thread': message[3], 'forum': message[4], 'isEdited': message[5]}
         

        return clear_dict({ 'post': post, 'thread': thread, 'forum': forum, 'author': user }), 200, None

    def post(self, id):
        new_message = self.json.get('message', None)
        id = int(id)
        message_update = db.prepare('''
            WITH updated AS (
                UPDATE message SET message = $2, isedited = sub.isedited OR sub.message IS DISTINCT FROM $2
                FROM (
                    SELECT * FROM message WHERE id = $1 FOR UPDATE
                ) as sub
                JOIN "user" ON sub.authorid = "user".id
                JOIN forum ON sub.forumid = forum.id
                RETURNING sub.authorid, sub.threadid, sub.forumid, 
                sub.created_on, message.message, message.isedited, slug, nickname
            )
            SELECT created_on, message, nickname, threadid, slug, isedited FROM updated''')
        # Consider returning less  {remove thread} (Optimisation)
        # Consider using a pre-update trigger to determine isedited and prevent needless message updates (Optimisation)

        if (new_message):
            message = message_update.first(id, new_message)
        else:
            message = db.prepare('''
                SELECT m.created_on, m.message, "user".nickname, m.threadid, forum.slug, isedited FROM (
                    SELECT created_on, message, authorid, threadid, forumid, isedited
                    FROM message WHERE id = $1
                ) as m
                JOIN "user" ON m.authorid = "user".id
                JOIN forum ON m.forumid = forum.id''').first(id)

        if not message:
            return error, 404
        #Consider returning less  {remove thread} (Optimisation)
        return { 'id': id, 'created': time_normalize(message[0]), 'message': message[1], 'author': message[2],
            'thread': message[3], 'forum': message[4], 'isEdited': message[5] }, 200, None