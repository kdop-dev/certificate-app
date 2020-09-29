#!/bin/bash
# python start
gunicorn --config gunicorn.conf.py wsgi:app
