# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import error
from start import db
from . import ApiHandler
from .. import schemas
from ..utils import clear_dict, time_normalize, timestamp



class ForumSlugThreads(ApiHandler):

    def get(self, slug):
        limit = self.args['limit']
        desc = bool(self.get_argument('desc', default='false'))
        desc = self.args.get('desc', False)
        print(desc)
        since = self.args.get('since')
        sort_option = ['ASC', 'DESC'][desc]
        print(self.args)
        since_cond = ''
        if since is not None:
            since = time_normalize(since.decode('utf-8'), db_format=True)

            since_cond = ' AND created_on ' + ['>=', '<='][desc] + 'TIMESTAMP' '\'' + str(since) + '\''


        forum_select = db.prepare('SELECT * FROM forum WHERE slug = $1::CITEXT')
        forum = forum_select.first(slug)
        print('forum')
        print(forum)
        if not forum:
            return error, 404
        thread_select = db.prepare('SELECT t.id, slug, created_on, message, title, nickname'
                                   ' FROM thread as t'
                                   ' JOIN "user" as u ON t.authorid = u.id  WHERE t.forumid = $1::BIGINT'
                                   + since_cond +
                                   ' ORDER BY created_on ' + sort_option +
                                   ' LIMIT $2')
        threads = []
        for id, slug, created, message, title, nickname in thread_select(forum[0], limit):
            threads.append(clear_dict({'id': id, 'slug': slug, 'created': time_normalize(created), 'message': message, 'title': title,
                                       'author': nickname, 'forum': forum[1]}))
        return threads, 200, None