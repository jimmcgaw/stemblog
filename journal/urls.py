from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # override the logout function so we redirect to login page after
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^account/$', views.account, name='account'),
    url(r'^article/new/', views.new_article, name='new_article'),
    url(r'^article/(?P<slug>[-\w]*)/$', views.view_article, name='view_article'),
]
