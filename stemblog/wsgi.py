"""
WSGI config for stemblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('~/.virtualenvs/stemblog/local/lib/python2.7/site-packages')
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(parent_dir)

# Activate your virtual env
try:
    activate_env = os.path.expanduser("/home/jim/.virtualenvs/stemblog/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))
except IOError:
    pass

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stemblog.settings")

application = get_wsgi_application()
