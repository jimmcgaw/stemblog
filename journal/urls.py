from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

app_name = 'journal'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # override the logout function so we redirect to login page after
    url(r'^logout/$', logout, {'next_page': '/login/'}),
    # url(r'^account/$', views.user_home, name='user_home'),
]
