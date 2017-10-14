# -*- coding: utf-8 -*-

import datetime

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/api'


DefinitionsForum={  
   'required':[  
      'title',
      'user',
      'slug'
   ],
   'type':'object',
   'description':'Информация о форуме.\n',
   'properties':{  
      'posts':{  
         'readOnly':True,
         'format':'int64',
         'type':'number',
         'example':200000,
         'description':'Общее кол-во сообщений в данном форуме.\n'
      },
      'title':{  
         'x-isnullable':False,
         'type':'string',
         'description':'Название форума.',
         'example':'Pirate stories'
      },
      'threads':{  
         'readOnly':True,
         'format':'int32',
         'type':'number',
         'example':200,
         'description':'Общее кол-во ветвей обсуждения в данном форуме.\n'
      },
      'slug':{  
         'x-isnullable':False,
         'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL), уникальное поле.',
         'format':'identity',
         'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
         'type':'string',
         'example':'pirate-stories'
      },
      'user':{  
         'x-isnullable':False,
         'format':'identity',
         'type':'string',
         'example':'j.sparrow',
         'description':'Nickname пользователя, который отвечает за форум.'
      }
   }
}

DefinitionsVote={  
   'required':[  
      'nickname',
      'voice'
   ],
   'type':'object',
   'description':'Информация о голосовании пользователя.\n',
   'properties':{  
      'voice':{  
         'x-isnullable':False,
         'enum':[  
            -1,
            1
         ],
         'type':'number',
         'description':'Отданный голос.',
         'format':'int32'
      },
      'nickname':{  
         'x-isnullable':False,
         'type':'string',
         'description':'Идентификатор пользователя.',
         'format':'identity'
      }
   }
}

DefinitionsThread={  
   'required':[  
      'title',
      'author',
      'message'
   ],
   'type':'object',
   'description':'Ветка обсуждения на форуме.\n',
   'properties':{  
      'votes':{  
         'readOnly':True,
         'type':'number',
         'description':'Кол-во голосов непосредственно за данное сообщение форума.',
         'format':'int32'
      },
      'forum':{  
         'readOnly':True,
         'format':'identity',
         'type':'string',
         'example':'pirate-stories',
         'description':'Форум, в котором расположена данная ветка обсуждения.'
      },
      'author':{  
         'x-isnullable':False,
         'format':'identity',
         'type':'string',
         'example':'j.sparrow',
         'description':'Пользователь, создавший данную тему.'
      },
      'title':{  
         'x-isnullable':False,
         'type':'string',
         'description':'Заголовок ветки обсуждения.',
         'example':'Davy Jones cache'
      },
      'created':{  
         'x-isnullable':True,
         'format':'date-time',
         'type':'string',
         'example':datetime.datetime(2017,
         1,
         1,
         0,
         0),
         'description':'Дата создания ветки на форуме.'
      },
      'id':{  
         'readOnly':True,
         'format':'int32',
         'type':'number',
         'example':42,
         'description':'Идентификатор ветки обсуждения.'
      },
      'message':{  
         'x-isnullable':False,
         'format':'text',
         'type':'string',
         'example':'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?',
         'description':'Описание ветки обсуждения.'
      },
      'slug':{  
         'readOnly':True,
         'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL).\nВ данной структуре slug опционален и не может быть числом.\n',
         'format':'identity',
         'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
         'type':'string',
         'example':'jones-cache'
      }
   }
}

DefinitionsUserupdate={  
   'type':'object',
   'description':'Информация о пользователе.\n',
   'properties':{  
      'fullname':{  
         'type':'string',
         'description':'Полное имя пользователя.',
         'example':'Captain Jack Sparrow'
      },
      'about':{  
         'format':'text',
         'type':'string',
         'example':'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!',
         'description':'Описание пользователя.'
      },
      'email':{  
         'format':'email',
         'type':'string',
         'example':'captaina@blackpearl.sea',
         'description':'Почтовый адрес пользователя (уникальное поле).'
      }
   }
}

DefinitionsThreadupdate={  
   'type':'object',
   'description':'Сообщение для обновления ветки обсуждения на форуме.\nПустые параметры остаются без изменений.\n',
   'properties':{  
      'message':{  
         'format':'text',
         'type':'string',
         'example':'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?',
         'description':'Описание ветки обсуждения.'
      },
      'title':{  
         'type':'string',
         'description':'Заголовок ветки обсуждения.',
         'example':'Davy Jones cache'
      }
   }
}

DefinitionsPost={  
   'required':[  
      'author',
      'message'
   ],
   'type':'object',
   'description':'Сообщение внутри ветки обсуждения на форуме.\n',
   'properties':{  
      'forum':{  
         'readOnly':True,
         'type':'string',
         'description':'Идентификатор форума (slug) данного сообещния.',
         'format':'identity'
      },
      'parent':{  
         'type':'number',
         'description':'Идентификатор родительского сообщения (0 - корневое сообщение обсуждения).\n',
         'format':'int64'
      },
      'author':{  
         'x-isnullable':False,
         'format':'identity',
         'type':'string',
         'example':'j.sparrow',
         'description':'Автор, написавший данное сообщение.'
      },
      'created':{  
         'x-isnullable':True,
         'format':'date-time',
         'type':'string',
         'readOnly':True,
         'description':'Дата создания сообщения на форуме.'
      },
      'thread':{  
         'readOnly':True,
         'type':'number',
         'description':'Идентификатор ветви (id) обсуждения данного сообещния.',
         'format':'int32'
      },
      'isEdited':{  
         'x-isnullable':False,
         'type':'boolean',
         'readOnly':True,
         'description':'Истина, если данное сообщение было изменено.'
      },
      'message':{  
         'x-isnullable':False,
         'format':'text',
         'type':'string',
         'example':'We should be afraid of the Kraken.',
         'description':'Собственно сообщение форума.'
      },
      'id':{  
         'readOnly':True,
         'type':'number',
         'description':'Идентификатор данного сообщения.',
         'format':'int64'
      }
   }
}

DefinitionsStatus={  
   'required':[  
      'user',
      'forum',
      'thread',
      'post'
   ],
   'type':'object',
   'properties':{  
      'forum':{  
         'x-isnullable':False,
         'format':'int32',
         'type':'number',
         'example':100,
         'description':'Кол-во разделов в базе данных.'
      },
      'post':{  
         'x-isnullable':False,
         'format':'int64',
         'type':'number',
         'example':1000000,
         'description':'Кол-во сообщений в базе данных.'
      },
      'user':{  
         'x-isnullable':False,
         'format':'int32',
         'type':'number',
         'example':1000,
         'description':'Кол-во пользователей в базе данных.'
      },
      'thread':{  
         'x-isnullable':False,
         'format':'int32',
         'type':'number',
         'example':1000,
         'description':'Кол-во веток обсуждения в базе данных.'
      }
   }
}

DefinitionsPostupdate={  
   'type':'object',
   'description':'Сообщение для обновления сообщения внутри ветки на форуме.\nПустые параметры остаются без изменений.\n',
   'properties':{  
      'message':{  
         'format':'text',
         'type':'string',
         'example':'We should be afraid of the Kraken.',
         'description':'Собственно сообщение форума.'
      }
   }
}

DefinitionsUser={  
   'required':[  
      'fullname',
      'email'
   ],
   'type':'object',
   'description':'Информация о пользователе.\n',
   'properties':{  
      'fullname':{  
         'x-isnullable':False,
         'type':'string',
         'description':'Полное имя пользователя.',
         'example':'Captain Jack Sparrow'
      },
      'nickname':{  
         'readOnly':True,
         'format':'identity',
         'type':'string',
         'example':'j.sparrow',
         'description':'Имя пользователя (уникальное поле).\nДанное поле допускает только латиницу, цифры и знак подчеркивания.\nСравнение имени регистронезависимо.\n'
      },
      'about':{  
         'format':'text',
         'type':'string',
         'example':'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!',
         'description':'Описание пользователя.'
      },
      'email':{  
         'x-isnullable':False,
         'format':'email',
         'type':'string',
         'example':'captaina@blackpearl.sea',
         'description':'Почтовый адрес пользователя (уникальное поле).'
      }
   }
}

DefinitionsError={  
   'type':'object',
   'properties':{  
      'message':{  
         'readOnly':True,
         'type':'string',
         'description':'Текстовое описание ошибки.\nВ процессе проверки API никаких проверок на содерижимое данного описание не делается.\n',
         'example':"Can't find user with id #42\n"
      }
   }
}

DefinitionsUsers={  
   'items':{  
      'required':[  
         'fullname',
         'email'
      ],
      'type':'object',
      'description':'Информация о пользователе.\n',
      'properties':{  
         'fullname':{  
            'x-isnullable':False,
            'type':'string',
            'description':'Полное имя пользователя.',
            'example':'Captain Jack Sparrow'
         },
         'nickname':{  
            'readOnly':True,
            'format':'identity',
            'type':'string',
            'example':'j.sparrow',
            'description':'Имя пользователя (уникальное поле).\nДанное поле допускает только латиницу, цифры и знак подчеркивания.\nСравнение имени регистронезависимо.\n'
         },
         'about':{  
            'format':'text',
            'type':'string',
            'example':'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!',
            'description':'Описание пользователя.'
         },
         'email':{  
            'x-isnullable':False,
            'format':'email',
            'type':'string',
            'example':'captaina@blackpearl.sea',
            'description':'Почтовый адрес пользователя (уникальное поле).'
         }
      }
   },
   'type':'array'
}

DefinitionsThreads={  
   'items':{  
      'required':[  
         'title',
         'author',
         'message'
      ],
      'type':'object',
      'description':'Ветка обсуждения на форуме.\n',
      'properties':{  
         'votes':{  
            'readOnly':True,
            'type':'number',
            'description':'Кол-во голосов непосредственно за данное сообщение форума.',
            'format':'int32'
         },
         'forum':{  
            'readOnly':True,
            'format':'identity',
            'type':'string',
            'example':'pirate-stories',
            'description':'Форум, в котором расположена данная ветка обсуждения.'
         },
         'author':{  
            'x-isnullable':False,
            'format':'identity',
            'type':'string',
            'example':'j.sparrow',
            'description':'Пользователь, создавший данную тему.'
         },
         'title':{  
            'x-isnullable':False,
            'type':'string',
            'description':'Заголовок ветки обсуждения.',
            'example':'Davy Jones cache'
         },
         'created':{  
            'x-isnullable':True,
            'format':'date-time',
            'type':'string',
            'example':datetime.datetime(2017,
            1,
            1,
            0,
            0            ),
            'description':'Дата создания ветки на форуме.'
         },
         'id':{  
            'readOnly':True,
            'format':'int32',
            'type':'number',
            'example':42,
            'description':'Идентификатор ветки обсуждения.'
         },
         'message':{  
            'x-isnullable':False,
            'format':'text',
            'type':'string',
            'example':'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?',
            'description':'Описание ветки обсуждения.'
         },
         'slug':{  
            'readOnly':True,
            'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL).\nВ данной структуре slug опционален и не может быть числом.\n',
            'format':'identity',
            'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
            'type':'string',
            'example':'jones-cache'
         }
      }
   },
   'type':'array'
}

DefinitionsPosts={  
   'items':{  
      'required':[  
         'author',
         'message'
      ],
      'type':'object',
      'description':'Сообщение внутри ветки обсуждения на форуме.\n',
      'properties':{  
         'forum':{  
            'readOnly':True,
            'type':'string',
            'description':'Идентификатор форума (slug) данного сообещния.',
            'format':'identity'
         },
         'parent':{  
            'type':'number',
            'description':'Идентификатор родительского сообщения (0 - корневое сообщение обсуждения).\n',
            'format':'int64'
         },
         'author':{  
            'x-isnullable':False,
            'format':'identity',
            'type':'string',
            'example':'j.sparrow',
            'description':'Автор, написавший данное сообщение.'
         },
         'created':{  
            'x-isnullable':True,
            'format':'date-time',
            'type':'string',
            'readOnly':True,
            'description':'Дата создания сообщения на форуме.'
         },
         'thread':{  
            'readOnly':True,
            'type':'number',
            'description':'Идентификатор ветви (id) обсуждения данного сообещния.',
            'format':'int32'
         },
         'isEdited':{  
            'x-isnullable':False,
            'type':'boolean',
            'readOnly':True,
            'description':'Истина, если данное сообщение было изменено.'
         },
         'message':{  
            'x-isnullable':False,
            'format':'text',
            'type':'string',
            'example':'We should be afraid of the Kraken.',
            'description':'Собственно сообщение форума.'
         },
         'id':{  
            'readOnly':True,
            'type':'number',
            'description':'Идентификатор данного сообщения.',
            'format':'int64'
         }
      }
   },
   'type':'array'
}

DefinitionsPostfull={  
   'type':'object',
   'description':'Полная информация о сообщении, включая связанные объекты.\n',
   'properties':{  
      'post':{  
         'required':[  
            'author',
            'message'
         ],
         'type':'object',
         'description':'Сообщение внутри ветки обсуждения на форуме.\n',
         'properties':{  
            'forum':{  
               'readOnly':True,
               'type':'string',
               'description':'Идентификатор форума (slug) данного сообещния.',
               'format':'identity'
            },
            'parent':{  
               'type':'number',
               'description':'Идентификатор родительского сообщения (0 - корневое сообщение обсуждения).\n',
               'format':'int64'
            },
            'author':{  
               'x-isnullable':False,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Автор, написавший данное сообщение.'
            },
            'created':{  
               'x-isnullable':True,
               'format':'date-time',
               'type':'string',
               'readOnly':True,
               'description':'Дата создания сообщения на форуме.'
            },
            'thread':{  
               'readOnly':True,
               'type':'number',
               'description':'Идентификатор ветви (id) обсуждения данного сообещния.',
               'format':'int32'
            },
            'isEdited':{  
               'x-isnullable':False,
               'type':'boolean',
               'readOnly':True,
               'description':'Истина, если данное сообщение было изменено.'
            },
            'message':{  
               'x-isnullable':False,
               'format':'text',
               'type':'string',
               'example':'We should be afraid of the Kraken.',
               'description':'Собственно сообщение форума.'
            },
            'id':{  
               'readOnly':True,
               'type':'number',
               'description':'Идентификатор данного сообщения.',
               'format':'int64'
            }
         }
      },
      'thread':{  
         'required':[  
            'title',
            'author',
            'message'
         ],
         'type':'object',
         'description':'Ветка обсуждения на форуме.\n',
         'properties':{  
            'votes':{  
               'readOnly':True,
               'type':'number',
               'description':'Кол-во голосов непосредственно за данное сообщение форума.',
               'format':'int32'
            },
            'forum':{  
               'readOnly':True,
               'format':'identity',
               'type':'string',
               'example':'pirate-stories',
               'description':'Форум, в котором расположена данная ветка обсуждения.'
            },
            'author':{  
               'x-isnullable':False,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Пользователь, создавший данную тему.'
            },
            'title':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Заголовок ветки обсуждения.',
               'example':'Davy Jones cache'
            },
            'created':{  
               'x-isnullable':True,
               'format':'date-time',
               'type':'string',
               'example':datetime.datetime(2017,
               1,
               1,
               0,
               0               ),
               'description':'Дата создания ветки на форуме.'
            },
            'id':{  
               'readOnly':True,
               'format':'int32',
               'type':'number',
               'example':42,
               'description':'Идентификатор ветки обсуждения.'
            },
            'message':{  
               'x-isnullable':False,
               'format':'text',
               'type':'string',
               'example':'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?',
               'description':'Описание ветки обсуждения.'
            },
            'slug':{  
               'readOnly':True,
               'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL).\nВ данной структуре slug опционален и не может быть числом.\n',
               'format':'identity',
               'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
               'type':'string',
               'example':'jones-cache'
            }
         }
      },
      'forum':{  
         'required':[  
            'title',
            'user',
            'slug'
         ],
         'type':'object',
         'description':'Информация о форуме.\n',
         'properties':{  
            'posts':{  
               'readOnly':True,
               'format':'int64',
               'type':'number',
               'example':200000,
               'description':'Общее кол-во сообщений в данном форуме.\n'
            },
            'title':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Название форума.',
               'example':'Pirate stories'
            },
            'threads':{  
               'readOnly':True,
               'format':'int32',
               'type':'number',
               'example':200,
               'description':'Общее кол-во ветвей обсуждения в данном форуме.\n'
            },
            'slug':{  
               'x-isnullable':False,
               'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL), уникальное поле.',
               'format':'identity',
               'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
               'type':'string',
               'example':'pirate-stories'
            },
            'user':{  
               'x-isnullable':False,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Nickname пользователя, который отвечает за форум.'
            }
         }
      },
      'author':{  
         'required':[  
            'fullname',
            'email'
         ],
         'type':'object',
         'description':'Информация о пользователе.\n',
         'properties':{  
            'fullname':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Полное имя пользователя.',
               'example':'Captain Jack Sparrow'
            },
            'nickname':{  
               'readOnly':True,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Имя пользователя (уникальное поле).\nДанное поле допускает только латиницу, цифры и знак подчеркивания.\nСравнение имени регистронезависимо.\n'
            },
            'about':{  
               'format':'text',
               'type':'string',
               'example':'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!',
               'description':'Описание пользователя.'
            },
            'email':{  
               'x-isnullable':False,
               'format':'email',
               'type':'string',
               'example':'captaina@blackpearl.sea',
               'description':'Почтовый адрес пользователя (уникальное поле).'
            }
         }
      }
   }
}

validators = {  
   ('forum_slug_users',
   'GET'   ):{  
      'args':{  
         'required':[  

         ],
         'properties':{  
            'since':{  
               'format':'identity',
               'type':'string',
               'description':'Идентификатор пользователя, с которого будут выводиться пользоватли\n(пользователь с данным идентификатором в результат не попадает).\n'
            },
            'limit':{  
               'format':'int32',
               'default':100,
               'maximum':10000,
               'minimum':1,
               'type':'number',
               'description':'Максимальное кол-во возвращаемых записей.'
            },
            'desc':{  
               'type':'boolean',
               'description':'Флаг сортировки по убыванию.\n'
            }
         }
      }
   },
   ('thread_slug_or_id_posts',
   'GET'   ):{  
      'args':{  
         'required':[  

         ],
         'properties':{  
            'sort':{  
               'description':'Вид сортировки:\n\n * flat - по дате, комментарии выводятся простым списком в порядке создания;\n * tree - древовидный, комментарии выводятся отсортированные в дереве\n   по N штук;\n * parent_tree - древовидные с пагинацией по родительским (parent_tree),\n   на странице N родительских комментов и все комментарии прикрепленные\n   к ним, в древвидном отображение.\n\nПодробности: https://park.mail.ru/blog/topic/view/1191/\n',
               'default':'flat',
               'enum':[  
                  'flat',
                  'tree',
                  'parent_tree'
               ],
               'type':'string'
            },
            'since':{  
               'format':'int64',
               'type':'number',
               'description':'Идентификатор поста, после которого будут выводиться записи\n(пост с данным идентификатором в результат не попадает).\n'
            },
            'limit':{  
               'format':'int32',
               'default':100,
               'maximum':10000,
               'minimum':1,
               'type':'number',
               'description':'Максимальное кол-во возвращаемых записей.'
            },
            'desc':{  
               'type':'boolean',
               'description':'Флаг сортировки по убыванию.\n'
            }
         }
      }
   },
   ('post_id_details',
   'POST'   ):{  
      'json':{  
         'type':'object',
         'description':'Сообщение для обновления сообщения внутри ветки на форуме.\nПустые параметры остаются без изменений.\n',
         'properties':{  
            'message':{  
               'format':'text',
               'type':'string',
               'example':'We should be afraid of the Kraken.',
               'description':'Собственно сообщение форума.'
            }
         }
      }
   },
   ('post_id_details',
   'GET'   ):{  
      'args':{  
         'required':[  

         ],
         'properties':{  
            'related':{  
               'items':{  
                  'enum':[  
                     'user',
                     'forum',
                     'thread'
                  ],
                  'type':'string'
               },
               'type':'array',
               'description':'Включение полной информации о соответвующем объекте сообщения.\n\nЕсли тип объекта не указан, то полная информация об этих объектах не\nпередаётся.\n'
            }
         }
      }
   },
   ('thread_slug_or_id_vote',
   'POST'   ):{  
      'json':{  
         'required':[  
            'nickname',
            'voice'
         ],
         'type':'object',
         'description':'Информация о голосовании пользователя.\n',
         'properties':{  
            'voice':{  
               'x-isnullable':False,
               'enum':[  
                  -1,
                  1
               ],
               'type':'number',
               'description':'Отданный голос.',
               'format':'int32'
            },
            'nickname':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Идентификатор пользователя.',
               'format':'identity'
            }
         }
      }
   },
   ('thread_slug_or_id_create',
   'POST'   ):{  
      'json':{  
         'items':{  
            'required':[  
               'author',
               'message'
            ],
            'type':'object',
            'description':'Сообщение внутри ветки обсуждения на форуме.\n',
            'properties':{  
               'forum':{  
                  'readOnly':True,
                  'type':'string',
                  'description':'Идентификатор форума (slug) данного сообещния.',
                  'format':'identity'
               },
               'parent':{  
                  'type':'number',
                  'description':'Идентификатор родительского сообщения (0 - корневое сообщение обсуждения).\n',
                  'format':'int64'
               },
               'author':{  
                  'x-isnullable':False,
                  'format':'identity',
                  'type':'string',
                  'example':'j.sparrow',
                  'description':'Автор, написавший данное сообщение.'
               },
               'created':{  
                  'x-isnullable':True,
                  'format':'date-time',
                  'type':'string',
                  'readOnly':True,
                  'description':'Дата создания сообщения на форуме.'
               },
               'thread':{  
                  'readOnly':True,
                  'type':'number',
                  'description':'Идентификатор ветви (id) обсуждения данного сообещния.',
                  'format':'int32'
               },
               'isEdited':{  
                  'x-isnullable':False,
                  'type':'boolean',
                  'readOnly':True,
                  'description':'Истина, если данное сообщение было изменено.'
               },
               'message':{  
                  'x-isnullable':False,
                  'format':'text',
                  'type':'string',
                  'example':'We should be afraid of the Kraken.',
                  'description':'Собственно сообщение форума.'
               },
               'id':{  
                  'readOnly':True,
                  'type':'number',
                  'description':'Идентификатор данного сообщения.',
                  'format':'int64'
               }
            }
         },
         'type':'array'
      }
   },
   ('thread_slug_or_id_details',
   'POST'   ):{  
      'json':{  
         'type':'object',
         'description':'Сообщение для обновления ветки обсуждения на форуме.\nПустые параметры остаются без изменений.\n',
         'properties':{  
            'message':{  
               'format':'text',
               'type':'string',
               'example':'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?',
               'description':'Описание ветки обсуждения.'
            },
            'title':{  
               'type':'string',
               'description':'Заголовок ветки обсуждения.',
               'example':'Davy Jones cache'
            }
         }
      }
   },
   ('forum_slug_create',
   'POST'   ):{  
      'json':{  
         'required':[  
            'title',
            'author',
            'message'
         ],
         'type':'object',
         'description':'Ветка обсуждения на форуме.\n',
         'properties':{  
            'votes':{  
               'readOnly':True,
               'type':'number',
               'description':'Кол-во голосов непосредственно за данное сообщение форума.',
               'format':'int32'
            },
            'forum':{  
               'readOnly':True,
               'format':'identity',
               'type':'string',
               'example':'pirate-stories',
               'description':'Форум, в котором расположена данная ветка обсуждения.'
            },
            'author':{  
               'x-isnullable':False,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Пользователь, создавший данную тему.'
            },
            'title':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Заголовок ветки обсуждения.',
               'example':'Davy Jones cache'
            },
            'created':{  
               'x-isnullable':True,
               'format':'date-time',
               'type':'string',
               'example':datetime.datetime(2017,
               1,
               1,
               0,
               0               ),
               'description':'Дата создания ветки на форуме.'
            },
            'id':{  
               'readOnly':True,
               'format':'int32',
               'type':'number',
               'example':42,
               'description':'Идентификатор ветки обсуждения.'
            },
            'message':{  
               'x-isnullable':False,
               'format':'text',
               'type':'string',
               'example':'An urgent need to reveal the hiding place of Davy Jones. Who is willing to help in this matter?',
               'description':'Описание ветки обсуждения.'
            },
            'slug':{  
               'readOnly':True,
               'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL).\nВ данной структуре slug опционален и не может быть числом.\n',
               'format':'identity',
               'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
               'type':'string',
               'example':'jones-cache'
            }
         }
      }
   },
   ('forum_slug_threads',
   'GET'   ):{  
      'args':{  
         'required':[  

         ],
         'properties':{  
            'since':{  
               'format':'date-time',
               'type':'string',
               'description':'Дата создания ветви обсуждения, с которой будут выводиться записи\n(ветвь обсуждения с указанной датой попадает в результат выборки).\n'
            },
            'limit':{  
               'format':'int32',
               'default':100,
               'maximum':10000,
               'minimum':1,
               'type':'number',
               'description':'Максимальное кол-во возвращаемых записей.'
            },
            'desc':{  
               'type':'boolean',
               'description':'Флаг сортировки по убыванию.\n'
            }
         }
      }
   },
   ('user_nickname_create',
   'POST'   ):{  
      'json':{  
         'required':[  
            'fullname',
            'email'
         ],
         'type':'object',
         'description':'Информация о пользователе.\n',
         'properties':{  
            'fullname':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Полное имя пользователя.',
               'example':'Captain Jack Sparrow'
            },
            'nickname':{  
               'readOnly':True,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Имя пользователя (уникальное поле).\nДанное поле допускает только латиницу, цифры и знак подчеркивания.\nСравнение имени регистронезависимо.\n'
            },
            'about':{  
               'format':'text',
               'type':'string',
               'example':'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!',
               'description':'Описание пользователя.'
            },
            'email':{  
               'x-isnullable':False,
               'format':'email',
               'type':'string',
               'example':'captaina@blackpearl.sea',
               'description':'Почтовый адрес пользователя (уникальное поле).'
            }
         }
      }
   },
   ('forum_create',
   'POST'   ):{  
      'json':{  
         'required':[  
            'title',
            'user',
            'slug'
         ],
         'type':'object',
         'description':'Информация о форуме.\n',
         'properties':{  
            'posts':{  
               'readOnly':True,
               'format':'int64',
               'type':'number',
               'example':200000,
               'description':'Общее кол-во сообщений в данном форуме.\n'
            },
            'title':{  
               'x-isnullable':False,
               'type':'string',
               'description':'Название форума.',
               'example':'Pirate stories'
            },
            'threads':{  
               'readOnly':True,
               'format':'int32',
               'type':'number',
               'example':200,
               'description':'Общее кол-во ветвей обсуждения в данном форуме.\n'
            },
            'slug':{  
               'x-isnullable':False,
               'description':'Человекопонятный URL (https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_URL), уникальное поле.',
               'format':'identity',
               'pattern':'^(\\d|\\w|-|_)*(\\w|-|_)(\\d|\\w|-|_)*$',
               'type':'string',
               'example':'pirate-stories'
            },
            'user':{  
               'x-isnullable':False,
               'format':'identity',
               'type':'string',
               'example':'j.sparrow',
               'description':'Nickname пользователя, который отвечает за форум.'
            }
         }
      }
   },
   ('user_nickname_profile',
   'POST'   ):{  
      'json':{  
         'type':'object',
         'description':'Информация о пользователе.\n',
         'properties':{  
            'fullname':{  
               'type':'string',
               'description':'Полное имя пользователя.',
               'example':'Captain Jack Sparrow'
            },
            'about':{  
               'format':'text',
               'type':'string',
               'example':'This is the day you will always remember as the day that you almost caught Captain Jack Sparrow!',
               'description':'Описание пользователя.'
            },
            'email':{  
               'format':'email',
               'type':'string',
               'example':'captaina@blackpearl.sea',
               'description':'Почтовый адрес пользователя (уникальное поле).'
            }
         }
      }
   }
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

