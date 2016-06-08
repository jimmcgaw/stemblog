"""stemblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', 'journal.views.index', name='index'),
    url(r'^journal/', include('journal.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    # override the logout function so we redirect to login page after
    url(r'^logout/$', logout, {'next_page': '/login/'}),

    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
