"""djangonetwork URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

from home.views import get_index, search
from accounts import urls as accounts_urls
from follow import urls as follow_urls
from mbox import urls as mbox_urls
from chatroom import urls as chatroom_urls
from games import urls as games_urls
from stream import urls as stream_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'^search/', search, name="search"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^follow/', include(follow_urls)),
    url(r'^mail/', include(mbox_urls)),
    url(r'^chatroom/', include(chatroom_urls)),
    url(r'^games/', include(games_urls)),
    url(r'^stream/', include(stream_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

