# -*- coding: utf-8 -*-

import datetime

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/api'


DefinitionsForum = {'required': ['title', 'user', 'slug'], 'type': 'object', 'description': u'\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0444\u043e\u0440\u0443\u043c\u0435.\n', 'properties': {'posts': {'readOnly': True, 'format': 'int64', 'type': 'number', 'example': 200000, 'description': u'\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b-\u0432\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0444\u043e\u0440\u0443\u043c\u0435.\n'}, 'title': {'x-isnullable': False, 'type': 'string', 'description': u'\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0440\u0443\u043c\u0430.', 'example': 'Pirate stories'}, 'threads': {'readOnly': True, 'format': 'int32', 'type': 'number', 'example': 200, 'description': u'\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b-\u0432\u043e \u0432\u0435\u0442\u0432\u0435\u0439 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0444\u043e\u0440\u0443\u043c\u0435.\n'}, 'slug': {'x-isnullable': False, 'description': u'\u0427\u0435\u043b\u043e\u0432\u0435\u043a\u043e\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL), \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u0435.', 'format': 'identity', 'pattern': '^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$', 'type': 'string', 'example': 'pirate-stories'}, 'user': {'x-isnullable': False, 'format': 'identity', 'type': 'string', 'example': 'j.sparrow', 'description': u'Nickname \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442 \u0437\u0430 \u0444\u043e\u0440\u0443\u043c.'}}}
DefinitionsVote = {'required': ['nickname', 'voice'], 'type': 'object', 'description': u'\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432\u0430\u043d\u0438\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.\n', 'properties': {'voice': {'x-isnullable': False, 'enum': [-1, 1], 'type': 'number', 'description': u'\u041e\u0442\u0434\u0430\u043d\u043d\u044b\u0439 \u0433\u043e\u043b\u043e\u0441.', 'format': 'int32'}, 'nickname': {'x-isnullable': False, 'type': 'string', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.', 'format': 'identity'}}}
DefinitionsThread = {'required': ['title', 'author', 'message'], 'type': 'object', 'description': u'\u0412\u0435\u0442\u043a\u0430 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u043d\u0430 \u0444\u043e\u0440\u0443\u043c\u0435.\n', 'properties': {'votes': {'readOnly': True, 'type': 'number', 'description': u'\u041a\u043e\u043b-\u0432\u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432 \u043d\u0435\u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0437\u0430 \u0434\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0444\u043e\u0440\u0443\u043c\u0430.', 'format': 'int32'}, 'forum': {'readOnly': True, 'format': 'identity', 'type': 'string', 'example': 'pirate-stories', 'description': u'\u0424\u043e\u0440\u0443\u043c, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0430 \u0434\u0430\u043d\u043d\u0430\u044f \u0432\u0435\u0442\u043a\u0430 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f.'}, 'author': {'x-isnullable': False, 'format': 'identity', 'type': 'string', 'example': 'j.sparrow', 'description': u'\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c, \u0441\u043e\u0437\u0434\u0430\u0432\u0448\u0438\u0439 \u0434\u0430\u043d\u043d\u0443\u044e \u0442\u0435\u043c\u0443.'}, 'title': {'x-isnullable': False, 'type': 'string', 'description': u'\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f.', 'example': 'Davy Jones cache'}, 'created': {'x-isnullable': True, 'format': 'date-time', 'type': 'string', 'example': datetime.datetime(2017, 1, 1, 0, 0), 'description': u'\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432\u0435\u0442\u043a\u0438 \u043d\u0430 \u0444\u043e\u0440\u0443\u043c\u0435.'}, 'id': {'readOnly': True, 'format': 'int32', 'type': 'number', 'example': 42, 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f.'}, 'message': {'x-isnullable': False, 'format': 'text', 'type': 'string', 'example': 'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?', 'description': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f.'}, 'slug': {'readOnly': True, 'description': u'\u0427\u0435\u043b\u043e\u0432\u0435\u043a\u043e\u043f\u043e\u043d\u044f\u0442\u043d\u044b\u0439 URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL).\n\u0412 \u0434\u0430\u043d\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0435 slug \u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u0435\u043d \u0438 \u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0447\u0438\u0441\u043b\u043e\u043c.\n', 'format': 'identity', 'pattern': '^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$', 'type': 'string', 'example': 'jones-cache'}}}
DefinitionsUserupdate = {'type': 'object', 'description': u'\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435.\n', 'properties': {'fullname': {'type': 'string', 'description': u'\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.', 'example': 'Captain Jack Sparrow'}, 'about': {'format': 'text', 'type': 'string', 'example': 'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!', 'description': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.'}, 'email': {'format': 'email', 'type': 'string', 'example': 'captaina@blackpearl.sea', 'description': u'\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f (\u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u0435).'}}}
DefinitionsThreadupdate = {'type': 'object', 'description': u'\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u043d\u0430 \u0444\u043e\u0440\u0443\u043c\u0435.\n\u041f\u0443\u0441\u0442\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0441\u0442\u0430\u044e\u0442\u0441\u044f \u0431\u0435\u0437 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0439.\n', 'properties': {'message': {'format': 'text', 'type': 'string', 'example': 'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?', 'description': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f.'}, 'title': {'type': 'string', 'description': u'\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f.', 'example': 'Davy Jones cache'}}}
DefinitionsPost = {'required': ['author', 'message'], 'type': 'object', 'description': u'\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u0435\u0442\u043a\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u043d\u0430 \u0444\u043e\u0440\u0443\u043c\u0435.\n', 'properties': {'forum': {'readOnly': True, 'type': 'string', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0444\u043e\u0440\u0443\u043c\u0430 (slug) \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0435\u0449\u043d\u0438\u044f.', 'format': 'identity'}, 'parent': {'type': 'number', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f (0 - \u043a\u043e\u0440\u043d\u0435\u0432\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f).\n', 'format': 'int64'}, 'author': {'x-isnullable': False, 'format': 'identity', 'type': 'string', 'example': 'j.sparrow', 'description': u'\u0410\u0432\u0442\u043e\u0440, \u043d\u0430\u043f\u0438\u0441\u0430\u0432\u0448\u0438\u0439 \u0434\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435.'}, 'created': {'x-isnullable': True, 'format': 'date-time', 'type': 'string', 'readOnly': True, 'description': u'\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u043d\u0430 \u0444\u043e\u0440\u0443\u043c\u0435.'}, 'thread': {'readOnly': True, 'type': 'number', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432\u0435\u0442\u0432\u0438 (id) \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0435\u0449\u043d\u0438\u044f.', 'format': 'int32'}, 'isEdited': {'x-isnullable': False, 'type': 'boolean', 'readOnly': True, 'description': u'\u0418\u0441\u0442\u0438\u043d\u0430, \u0435\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0431\u044b\u043b\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u043e.'}, 'message': {'x-isnullable': False, 'format': 'text', 'type': 'string', 'example': 'We should be afraid of the Kraken.', 'description': u'\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0444\u043e\u0440\u0443\u043c\u0430.'}, 'id': {'readOnly': True, 'type': 'number', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f.', 'format': 'int64'}}}
DefinitionsStatus = {'required': ['user', 'forum', 'thread', 'post'], 'type': 'object', 'properties': {'forum': {'x-isnullable': False, 'format': 'int32', 'type': 'number', 'example': 100, 'description': u'\u041a\u043e\u043b-\u0432\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u043e\u0432 \u0432 \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445.'}, 'post': {'x-isnullable': False, 'format': 'int64', 'type': 'number', 'example': 1000000, 'description': u'\u041a\u043e\u043b-\u0432\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u0432 \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445.'}, 'user': {'x-isnullable': False, 'format': 'int32', 'type': 'number', 'example': 1000, 'description': u'\u041a\u043e\u043b-\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0432 \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445.'}, 'thread': {'x-isnullable': False, 'format': 'int32', 'type': 'number', 'example': 1000, 'description': u'\u041a\u043e\u043b-\u0432\u043e \u0432\u0435\u0442\u043e\u043a \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u0432 \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445.'}}}
DefinitionsPostupdate = {'type': 'object', 'description': u'\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u0435\u0442\u043a\u0438 \u043d\u0430 \u0444\u043e\u0440\u0443\u043c\u0435.\n\u041f\u0443\u0441\u0442\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0441\u0442\u0430\u044e\u0442\u0441\u044f \u0431\u0435\u0437 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0439.\n', 'properties': {'message': {'format': 'text', 'type': 'string', 'example': 'We should be afraid of the Kraken.', 'description': u'\u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0444\u043e\u0440\u0443\u043c\u0430.'}}}
DefinitionsUser = {'required': ['fullname', 'email'], 'type': 'object', 'description': u'\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435.\n', 'properties': {'fullname': {'x-isnullable': False, 'type': 'string', 'description': u'\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.', 'example': 'Captain Jack Sparrow'}, 'nickname': {'readOnly': True, 'format': 'identity', 'type': 'string', 'example': 'j.sparrow', 'description': u'\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f (\u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u0435).\n\u0414\u0430\u043d\u043d\u043e\u0435 \u043f\u043e\u043b\u0435 \u0434\u043e\u043f\u0443\u0441\u043a\u0430\u0435\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u043b\u0430\u0442\u0438\u043d\u0438\u0446\u0443, \u0446\u0438\u0444\u0440\u044b \u0438 \u0437\u043d\u0430\u043a \u043f\u043e\u0434\u0447\u0435\u0440\u043a\u0438\u0432\u0430\u043d\u0438\u044f.\n\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u043e\u043d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e.\n'}, 'about': {'format': 'text', 'type': 'string', 'example': 'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!', 'description': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f.'}, 'email': {'x-isnullable': False, 'format': 'email', 'type': 'string', 'example': 'captaina@blackpearl.sea', 'description': u'\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f (\u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u0435).'}}}
DefinitionsError = {'type': 'object', 'properties': {'message': {'readOnly': True, 'type': 'string', 'description': u'\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0448\u0438\u0431\u043a\u0438.\n\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 API \u043d\u0438\u043a\u0430\u043a\u0438\u0445 \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u043a \u043d\u0430 \u0441\u043e\u0434\u0435\u0440\u0438\u0436\u0438\u043c\u043e\u0435 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0435 \u0434\u0435\u043b\u0430\u0435\u0442\u0441\u044f.\n', 'example': "Can't find user with id #42\n"}}}
DefinitionsUsers = {'items': DefinitionsUser, 'type': 'array'}
DefinitionsThreads = {'items': DefinitionsThread, 'type': 'array'}
DefinitionsPosts = {'items': DefinitionsPost, 'type': 'array'}
DefinitionsPostfull = {'type': 'object', 'description': u'\u041f\u043e\u043b\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0438, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u044b\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u044b.\n', 'properties': {'post': DefinitionsPost, 'thread': DefinitionsThread, 'forum': DefinitionsForum, 'author': DefinitionsUser}}

validators = {
    ('forum_slug_users', 'GET'): {'args': {'required': [], 'properties': {'since': {'format': 'identity', 'type': 'string', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u043b\u0438\n(\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u0441 \u0434\u0430\u043d\u043d\u044b\u043c \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u043c \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0435 \u043f\u043e\u043f\u0430\u0434\u0430\u0435\u0442).\n'}, 'limit': {'format': 'int32', 'default': 100, 'maximum': 10000, 'minimum': 1, 'type': 'number', 'description': u'\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u043c\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439.'}, 'desc': {'type': 'boolean', 'description': u'\u0424\u043b\u0430\u0433 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e.\n'}}}},
    ('thread_slug_or_id_posts', 'GET'): {'args': {'required': [], 'properties': {'sort': {'description': u'\u0412\u0438\u0434 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438:\n\n * flat - \u043f\u043e \u0434\u0430\u0442\u0435, \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u0432\u044b\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u043f\u0440\u043e\u0441\u0442\u044b\u043c \u0441\u043f\u0438\u0441\u043a\u043e\u043c \u0432 \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f;\n * tree - \u0434\u0440\u0435\u0432\u043e\u0432\u0438\u0434\u043d\u044b\u0439, \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u0432\u044b\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u043e\u0442\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0432 \u0434\u0435\u0440\u0435\u0432\u0435\n   \u043f\u043e N \u0448\u0442\u0443\u043a;\n * parent_tree - \u0434\u0440\u0435\u0432\u043e\u0432\u0438\u0434\u043d\u044b\u0435 \u0441 \u043f\u0430\u0433\u0438\u043d\u0430\u0446\u0438\u0435\u0439 \u043f\u043e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u043c (parent_tree),\n   \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 N \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0445 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u043e\u0432 \u0438 \u0432\u0441\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0435\n   \u043a \u043d\u0438\u043c, \u0432 \u0434\u0440\u0435\u0432\u0432\u0438\u0434\u043d\u043e\u043c \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435.\n\n\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e\u0441\u0442\u0438: https://park.mail.ru/blog/topic/view/1191/\n', 'default': 'flat', 'enum': ['flat', 'tree', 'parent_tree'], 'type': 'string'}, 'since': {'format': 'int64', 'type': 'number', 'description': u'\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e\u0441\u0442\u0430, \u043f\u043e\u0441\u043b\u0435 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u0437\u0430\u043f\u0438\u0441\u0438\n(\u043f\u043e\u0441\u0442 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u043c \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043d\u0435 \u043f\u043e\u043f\u0430\u0434\u0430\u0435\u0442).\n'}, 'limit': {'format': 'int32', 'default': 100, 'maximum': 10000, 'minimum': 1, 'type': 'number', 'description': u'\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u043c\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439.'}, 'desc': {'type': 'boolean', 'description': u'\u0424\u043b\u0430\u0433 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e.\n'}}}},
    ('post_id_details', 'POST'): {'json': DefinitionsPostupdate},
    ('post_id_details', 'GET'): {'args': {'required': [], 'properties': {'related': {'items': {'enum': ['user', 'forum', 'thread'], 'type': 'string'}, 'type': 'array', 'description': u'\u0412\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0432\u0443\u044e\u0449\u0435\u043c \u043e\u0431\u044a\u0435\u043a\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f.\n\n\u0415\u0441\u043b\u0438 \u0442\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d, \u0442\u043e \u043f\u043e\u043b\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u044d\u0442\u0438\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445 \u043d\u0435\n\u043f\u0435\u0440\u0435\u0434\u0430\u0451\u0442\u0441\u044f.\n'}}}},
    ('thread_slug_or_id_vote', 'POST'): {'json': DefinitionsVote},
    ('thread_slug_or_id_create', 'POST'): {'json': DefinitionsPosts},
    ('thread_slug_or_id_details', 'POST'): {'json': DefinitionsThreadupdate},
    ('forum_slug_create', 'POST'): {'json': DefinitionsThread},
    ('forum_slug_threads', 'GET'): {'args': {'required': [], 'properties': {'since': {'format': 'date-time', 'type': 'string', 'description': u'\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0432\u0435\u0442\u0432\u0438 \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u0437\u0430\u043f\u0438\u0441\u0438\n(\u0432\u0435\u0442\u0432\u044c \u043e\u0431\u0441\u0443\u0436\u0434\u0435\u043d\u0438\u044f \u0441 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0439 \u0434\u0430\u0442\u043e\u0439 \u043f\u043e\u043f\u0430\u0434\u0430\u0435\u0442 \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u044b\u0431\u043e\u0440\u043a\u0438).\n'}, 'limit': {'format': 'int32', 'default': 100, 'maximum': 10000, 'minimum': 1, 'type': 'number', 'description': u'\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b-\u0432\u043e \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u043c\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439.'}, 'desc': {'type': 'boolean', 'description': u'\u0424\u043b\u0430\u0433 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e.\n'}}}},
    ('user_nickname_create', 'POST'): {'json': DefinitionsUser},
    ('forum_create', 'POST'): {'json': DefinitionsForum},
    ('user_nickname_profile', 'POST'): {'json': DefinitionsUserupdate},
}

filters = {
    ('service_status', 'GET'): {200: {'headers': None, 'schema': DefinitionsStatus}},
    ('forum_slug_users', 'GET'): {200: {'headers': None, 'schema': DefinitionsUsers}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('thread_slug_or_id_posts', 'GET'): {200: {'headers': None, 'schema': DefinitionsPosts}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('post_id_details', 'POST'): {200: {'headers': None, 'schema': DefinitionsPost}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('post_id_details', 'GET'): {200: {'headers': None, 'schema': DefinitionsPostfull}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('thread_slug_or_id_vote', 'POST'): {200: {'headers': None, 'schema': DefinitionsThread}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('thread_slug_or_id_create', 'POST'): {201: {'headers': None, 'schema': DefinitionsPosts}, 404: {'headers': None, 'schema': DefinitionsError}, 409: {'headers': None, 'schema': DefinitionsError}},
    ('service_clear', 'POST'): {200: {'headers': None, 'schema': None}},
    ('thread_slug_or_id_details', 'POST'): {200: {'headers': None, 'schema': DefinitionsThread}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('thread_slug_or_id_details', 'GET'): {200: {'headers': None, 'schema': DefinitionsThread}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('forum_slug_create', 'POST'): {201: {'headers': None, 'schema': DefinitionsThread}, 404: {'headers': None, 'schema': DefinitionsError}, 409: {'headers': None, 'schema': DefinitionsThread}},
    ('forum_slug_details', 'GET'): {200: {'headers': None, 'schema': DefinitionsForum}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('forum_slug_threads', 'GET'): {200: {'headers': None, 'schema': DefinitionsThreads}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('user_nickname_create', 'POST'): {201: {'headers': None, 'schema': DefinitionsUser}, 409: {'headers': None, 'schema': DefinitionsUsers}},
    ('forum_create', 'POST'): {201: {'headers': None, 'schema': DefinitionsForum}, 404: {'headers': None, 'schema': DefinitionsError}, 409: {'headers': None, 'schema': DefinitionsForum}},
    ('user_nickname_profile', 'POST'): {200: {'headers': None, 'schema': DefinitionsUser}, 409: {'headers': None, 'schema': DefinitionsError}, 404: {'headers': None, 'schema': DefinitionsError}},
    ('user_nickname_profile', 'GET'): {200: {'headers': None, 'schema': DefinitionsUser}, 404: {'headers': None, 'schema': DefinitionsError}},
}

scopes = {
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):

    import six

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

