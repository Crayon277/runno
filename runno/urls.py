from django.conf.urls import patterns, include, url

from django.contrib import admin
#from views import *
from unno.views import *

#from views import *
from django.conf.urls.static import static

from django.conf import settings

import os

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'runno.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS}),
    url(r'^comments/',include('django.contrib.comments.urls')),


    #url(r'^hello/$',hello),

    url(r'^$',about),
    url(r'^resume/$',resume),
    url(r'^just_run/$',run),
    url(r'^unno/$',unno),
    url(r'^never_say_no/$',never_say_no),
    url(r'^now_or_never/$',now_or_never),
    url(r'^blog/$',blog),
    url(r'^blog/(?P<id>\d+)/$',blog_show,name = 'detailblog'),
    url(r'^blog/tag/(?P<id>\d+)/$',blog_filter,name = 'filtrblog'),
    url(r'^blog/add/$',blog_add,name = 'addblog'),
    url(r'^blog/(?P<id>\d+)/update/$',blog_update,name = 'updateblog'),
    url(r'^blog/(?P<id>\d+)/del/$', blog_del,name = 'delblog'),
    
    url(r'^fire_work/$',fire_work,name = 'firework'),


)
#urlpatterns += static (settings.STATIC_URL,document_root = settings.STATIC_ROOT)
