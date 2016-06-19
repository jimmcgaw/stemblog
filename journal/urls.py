from django.conf.urls import url


app_name = 'journal'

urlpatterns = [
    url(r'^$', 'journal.views.account', name='account'),
    url(r'^article/new/$', 'journal.views.new_article', name='new_article'),
    url(r'^article/edit/(?P<article_id>[-\d]+)/$', 'journal.views.edit_article', name='edit_article'),
    url(r'^article/(?P<slug>[-\w]+)/$', 'journal.views.view_article', name='view_article'),
]
