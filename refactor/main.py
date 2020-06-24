#!/usr/bin/env python

from route import route
from werkzeug.serving import run_simple


if __name__ == "__main__":
    run_simple('', 8000, route, use_reloader=True)
