from django.conf.urls import url
from django.contrib.auth.views import logout

app_name = 'journal'

urlpatterns = [
    url(r'^$', 'journal.views.index', name='index'),
    # override the logout function so we redirect to login page after
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^account/$', 'journal.views.account', name='account'),
    url(r'^article/new/$', 'journal.views.new_article', name='new_article'),
    url(r'^article/(?P<slug>[-\w]+)/$', 'journal.views.view_article', name='view_article'),
]
