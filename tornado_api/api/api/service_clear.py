# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ServiceClear(ApiHandler):

    def post(self):

        return None, 200, None