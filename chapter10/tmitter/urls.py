# -*- coding: utf-8 -*-
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include 
from django.contrib import admin
from tmitter.mvc.feed import RSSRecentNotes,RSSUserRecentNotes
import tmitter, django
import tmitter.mvc.views
import django.contrib.syndication.views
import django.views.static
import django.conf.urls
import django.conf.urls.i18n
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

rss_feeds = {
    'recent': RSSRecentNotes,
}

rss_user_feeds = {
    'recent': RSSUserRecentNotes,
}

urlpatterns = [
    # Example:
    # (r'^note/', include('note.foo.urls')),
    url(r'^$',tmitter.mvc.views.index),
    url(r'^p/(?P<_page_index>\d+)/$',tmitter.mvc.views.index_page),
    url(r'^user/$',tmitter.mvc.views.index_user_self),
#    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/$',tmitter.mvc.views.index_user, name= "tmitter-mvc-views-index_user"),
    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/$',tmitter.mvc.views.index_user, name= "tmitter-mvc-views-index_user"),
    url(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/(?P<_page_index>\d+)/$',tmitter.mvc.views.index_user_page),
    url(r'^users/$',tmitter.mvc.views.users_index),
    url(r'^users/(?P<_page_index>\d+)/$',tmitter.mvc.views.users_list),
    url(r'^signin/$',tmitter.mvc.views.signin),
    url(r'^signout/$',tmitter.mvc.views.signout),
    url(r'^signup/$',tmitter.mvc.views.signup),
    url(r'^settings/$',tmitter.mvc.views.settings, name ='tmitter_mvc_views_settings'),
    url(r'^message/(?P<_id>\d+)/$',tmitter.mvc.views.detail, name = "tmitter-mvc-views-detail"),
    url(r'^message/(?P<_id>\d+)/delete/$',tmitter.mvc.views.detail_delete, name = "tmitter-mvc-views-detail_delete"),
    url(r'^friend/add/(?P<_username>[a-zA-Z\-_\d]+)',tmitter.mvc.views.friend_add, name="tmitter-mvc-views-friend_add"),
    url(r'^friend/remove/(?P<_username>[a-zA-Z\-_\d]+)',tmitter.mvc.views.friend_remove),
    url(r'^api/note/add/',tmitter.mvc.views.api_note_add),
    # Uncomment this for admin:
    #url(r'^admin/(.*)',admin.site.urls),
    url(r'^admin/',admin.site.urls),
    url(r'^feed/rss/(?P<url>.*)/$', django.contrib.syndication.views.Feed, {'feed_dict': rss_feeds}),
    url(r'^user/feed/rss/(?P<url>.*)/$', django.contrib.syndication.views.Feed, {'feed_dict': rss_user_feeds}),	
#    url(r'^statics/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^i18n/', django.conf.urls.i18n.i18n_patterns),

]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

