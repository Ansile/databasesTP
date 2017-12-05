# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from .db_queries import db
from . import ApiHandler
from .. import schemas
from . import error

class ForumSlugDetails(ApiHandler):

    def get(self, slug):
        forum_select = db.prepare('SELECT * FROM forum WHERE slug = $1::CITEXT')
        forum = forum_select.first(slug)
        
        if forum:
            user_select = db.prepare('SELECT * FROM "user" WHERE id = $1::BIGINT')
            user = user_select.first(forum[3])
            postcount = db.prepare('SELECT COUNT(id) FROM message WHERE forumid = $1').first(forum[0])
            threadcount = db.prepare('SELECT COUNT(id) FROM thread WHERE forumid = $1').first(forum[0])
            username = user[1]
            return {'slug': forum[1], 'user': username, 'title': forum[2], 'posts': postcount, 'threads': threadcount}, 200
        return error, 404