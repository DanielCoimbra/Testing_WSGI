#!/usr/bin/env python
# -*- coding: utf-8 -*-
if __name__ == "__main__":
            
    from werkzeug.serving import run_simple
    from route import route

    app = route
    run_simple('localhost', 8000, app, use_reloader=True)
