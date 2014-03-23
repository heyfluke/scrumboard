#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################
# File: settings/__init__.py
# Author: laoyc <fluke.l@gmail.com>
###########################################


from .base import *
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-dist.py?)' % exc.args[0]])
    raise exc

