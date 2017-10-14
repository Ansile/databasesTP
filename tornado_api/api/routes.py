# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.service_status import ServiceStatus
from .api.forum_slug_users import ForumSlugUsers
from .api.thread_slug_or_id_posts import ThreadSlugOrIdPosts
from .api.post_id_details import PostIdDetails
from .api.thread_slug_or_id_vote import ThreadSlugOrIdVote
from .api.thread_slug_or_id_create import ThreadSlugOrIdCreate
from .api.service_clear import ServiceClear
from .api.thread_slug_or_id_details import ThreadSlugOrIdDetails
from .api.forum_slug_create import ForumSlugCreate
from .api.forum_slug_details import ForumSlugDetails
from .api.forum_slug_threads import ForumSlugThreads
from .api.user_nickname_create import UserNicknameCreate
from .api.forum_create import ForumCreate
from .api.user_nickname_profile import UserNicknameProfile


url_prefix = 'api'

routes = [
    dict(resource=ServiceStatus, urls=[r"/service/status"], endpoint='service_status'),
    dict(resource=ForumSlugUsers, urls=[r"/forum/(?P<slug>[^/]+?)/users"], endpoint='forum_slug_users'),
    dict(resource=ThreadSlugOrIdPosts, urls=[r"/thread/(?P<slug_or_id>[^/]+?)/posts"], endpoint='thread_slug_or_id_posts'),
    dict(resource=PostIdDetails, urls=[r"/post/(?P<id>[^/]+?)/details"], endpoint='post_id_details'),
    dict(resource=ThreadSlugOrIdVote, urls=[r"/thread/(?P<slug_or_id>[^/]+?)/vote"], endpoint='thread_slug_or_id_vote'),
    dict(resource=ThreadSlugOrIdCreate, urls=[r"/thread/(?P<slug_or_id>[^/]+?)/create"], endpoint='thread_slug_or_id_create'),
    dict(resource=ServiceClear, urls=[r"/service/clear"], endpoint='service_clear'),
    dict(resource=ThreadSlugOrIdDetails, urls=[r"/thread/(?P<slug_or_id>[^/]+?)/details"], endpoint='thread_slug_or_id_details'),
    dict(resource=ForumSlugCreate, urls=[r"/forum/(?P<slug>[^/]+?)/create"], endpoint='forum_slug_create'),
    dict(resource=ForumSlugDetails, urls=[r"/forum/(?P<slug>[^/]+?)/details"], endpoint='forum_slug_details'),
    dict(resource=ForumSlugThreads, urls=[r"/forum/(?P<slug>[^/]+?)/threads"], endpoint='forum_slug_threads'),
    dict(resource=UserNicknameCreate, urls=[r"/user/(?P<nickname>[^/]+?)/create"], endpoint='user_nickname_create'),
    dict(resource=ForumCreate, urls=[r"/forum/create"], endpoint='forum_create'),
    dict(resource=UserNicknameProfile, urls=[r"/user/(?P<nickname>[^/]+?)/profile"], endpoint='user_nickname_profile'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass