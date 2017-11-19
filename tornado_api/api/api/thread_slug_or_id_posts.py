# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from start import db
from . import ApiHandler
from .. import schemas
from ..utils import time_normalize, int_convert, slug_and_id
Debug = False


class ThreadSlugOrIdPosts(ApiHandler):

    def get(self, slug_or_id):
        thread_slug, thread_id = slug_and_id(slug_or_id)
        sort = self.args.get('sort')
        since = self.args.get('since')
        print(sort)
        if not isinstance(sort, str):
            sort = sort.decode('utf-8')
        desc = self.args.get('desc', False)
        if (desc):
            sort_option = 'DESC'
        else:
            sort_option = 'ASC'

        print(sort_option)
        limit = self.args['limit']

        if since:
            # since = time_normalize(since)
            since_cond_message = ' AND message.id ' + ['>', '<'][desc] + ' $3::BIGINT'
            since_cond_m = ' WHERE m.id ' + ['>', '<'][desc] + ' $3::BIGINT'
            since_cond_tree = 'WHERE m.parenttree || m.id > (SELECT parenttree || id FROM message WHERE id = $3::BIGINT)' #AND (message.parenttree[2] ' + ['>', '<'][desc] + ' $3::BIGINT OR message.parenttree[2] IS NULL) '


        else:
            since_cond_tree = since_cond_message = since_cond_m = ''
        select_fields = 'SELECT m.id, m.created_on, m.message, m.threadid, m.parentid, "user".nickname, forum.slug'
        inner_select_fields = '''SELECT message.id, message.created_on, message.threadid, message.message,
                                 message.parentid, message.authorid, message.forumid'''
        inner_select_fields_tree = inner_select_fields + ', message.parenttree'
        if sort == 'flat':
            if thread_slug:
                message_select = db.prepare('''
                    {select_fields}
                     FROM (
                         {select_inner}
                         FROM message JOIN thread ON message.threadid = thread.id 
                         WHERE thread.slug = $1 {since} ORDER BY message.id {sort} LIMIT $2
                     ) as m
                     JOIN "user" ON "user".id = m.authorid
                     JOIN forum ON m.forumid = forum.id
                     ORDER BY m.id  {sort}'''.format(sort = sort_option, since = since_cond_message, select_fields = select_fields, select_inner = inner_select_fields)) # TODO: check how the fuck does this work
                if since:
                    messages = message_select(thread_slug, limit, since)
                else:
                    messages = message_select(thread_slug, limit)
            else:
                message_select = db.prepare('''
                    {select_fields}
                     FROM (
                        {select_inner}
                        FROM message WHERE message.threadid = $1 {since} ORDER BY message.id {sort} LIMIT $2
                     ) as m
                     JOIN "user" ON "user".id = m.authorid
                     JOIN forum ON m.forumid = forum.id
                     ORDER BY m.id {sort}'''.format(sort = sort_option, since = since_cond_message, select_fields = select_fields, select_inner = inner_select_fields))
                if since:
                    messages = message_select(thread_id, limit, since)
                else:
                    messages = message_select(thread_id, limit)
        elif sort == 'tree':
            if thread_slug:
                message_select = db.prepare('''
                        {select_fields}
                         FROM (
                             {select_inner} 
                             FROM message JOIN thread ON message.threadid = thread.id 
                             WHERE thread.slug = $1 ORDER BY message.parenttree || message.id {sort}
                         ) as m
                         JOIN "user" ON "user".id = m.authorid
                         JOIN forum ON m.forumid = forum.id
                         {since}
                         ORDER BY m.parenttree || m.id {sort} LIMIT $2'''.format(sort = sort_option, since = since_cond_tree, select_fields = select_fields, select_inner = inner_select_fields_tree))
                if since:
                    messages = message_select(thread_slug, limit, since)
                else:
                    messages = message_select(thread_slug, limit)
            else:
                message_select = db.prepare('''
                        {select_fields}
                         FROM (
                             {select_inner}
                             FROM message
                             WHERE message.threadid = $1 ORDER BY message.parenttree || message.id {sort}
                         ) as m
                         JOIN "user" ON "user".id = m.authorid
                         JOIN forum ON m.forumid = forum.id
                         {since}
                         ORDER BY m.parenttree || m.id {sort} LIMIT $2'''.format(sort = sort_option, since = since_cond_tree, select_fields = select_fields, select_inner = inner_select_fields_tree))
                if since:
                    messages = message_select(thread_id, limit, since)
                else:
                    messages = message_select(thread_id, limit)
        elif sort == 'parent_tree':  #TODO: fix since
            if thread_slug:
                message_select = db.prepare('''
                        {select_fields}
                         FROM (
                             {select_inner}
                             FROM message JOIN thread ON message.threadid = thread.id 
                             WHERE message.parenttree[2] IN
                             (SELECT message.id
                             FROM message JOIN thread ON message.threadid = thread.id 
                             WHERE thread.slug = $1 AND message.parentid is NULL ORDER BY message.id LIMIT $2)
                             UNION 
                             ({select_inner}
                             FROM message JOIN thread ON message.threadid = thread.id 
                             WHERE thread.slug = $1 AND message.parentid is NULL ORDER BY message.id LIMIT $2)
                         ) as m
                         JOIN "user" ON "user".id = m.authorid
                         JOIN forum ON m.forumid = forum.id
                         {since}
                         ORDER BY m.parenttree || m.id {sort}'''.format(sort = sort_option, since = since_cond_message, select_fields = select_fields, select_inner = inner_select_fields_tree))
                if since:
                    messages = message_select(thread_slug, limit, since)
                else:
                    messages = message_select(thread_slug, limit)
            else:
                message_select = db.prepare('''
                    {select_fields}
                     FROM (
                         {select_inner}
                         FROM message
                         WHERE message.parenttree[2] IN
                         (SELECT message.id
                         FROM message WHERE message.threadid = $1 
                         AND message.parentid is NULL ORDER BY message.id LIMIT $2)
                         UNION 
                         ({select_inner}
                         FROM message WHERE message.threadid = $1 
                         AND message.parentid is NULL ORDER BY message.id LIMIT $2)
                     ) as m
                     JOIN "user" ON "user".id = m.authorid
                     JOIN forum ON m.forumid = forum.id
                     {since}
                     ORDER BY m.parenttree || m.id {sort}'''.format(sort = sort_option, since = since_cond_message, select_fields = select_fields, select_inner = inner_select_fields_tree))
                if since:
                    messages = message_select(thread_id, limit, since)
                else:
                    messages = message_select(thread_id, limit)

        result = []
        for x in messages:
            message = {'id': x[0], 'created': time_normalize(x[1], json_format=True), 'message': x[2],
                       'thread': x[3], 'parent': int_convert(x[4]), 'author': x[5], 'forum': x[6]}
            result.append(message)
        if Debug:
            print('messages')
            print(messages)
        return result, 200