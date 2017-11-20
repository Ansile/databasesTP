# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from start import db
from . import error
from . import ApiHandler
from .. import schemas


class ForumSlugUsers(ApiHandler):

    def get(self, slug):
    	desc = self.args.get('desc', False)
    	since = self.args.get('since')
    	limit = self.args.get('limit')
    	forum_id = db.prepare('SELECT id from forum WHERE slug = $1').first(slug)
    	if not forum_id:
    		return error, 404
    	sort_option = ['ASC', 'DESC'][desc]
    	comp = ['>', '<'][desc]

    	if since:
    		since = since.decode('utf-8')
    		since_cond = 'AND "user".nickname ' + comp + '$3'

    	users_select = db.prepare('''
    		SELECT nickname, about, email, fullname, lower(nickname) as sorting from thread 
    		JOIN "user" on "user".id = thread.authorid 
    		WHERE thread.forumid = $1
    		{since}
    		UNION
    		SELECT nickname, about, email, fullname, lower(nickname) as sorting from message 
    		JOIN "user" on "user".id = message.authorid 
    		WHERE message.forumid = $1
    		{since}
    		ORDER BY sorting {sort} {limit}
    		'''.format(sort = sort_option, limit = 'LIMIT $2' if limit else '', since = since_cond if since else ''))
    	if limit:
    		if since:
    			users = users_select(forum_id, limit, since)
    		else:
    			users = users_select(forum_id, limit)
    	else:
    		if since:
    			raise Exception('Not Implemented')
    		users = users_select(forum_id)
    	
    	result = [{'nickname': user[0], 'about': user[1], 'email': user[2], 'fullname': user[3]} for user in users]
    	return result, 200, None