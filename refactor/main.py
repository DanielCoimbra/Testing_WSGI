#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from route import route

app = route
run_simple('localhost', 8000, app, use_reloader=True)
