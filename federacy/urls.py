from django.conf.urls.defaults import *

urlpatterns = patterns('socialite.federacy.views',
    (r'^$', 'index'),
    (r'^(?P<msg_id>\d+)/$', 'detail'),
    (r'^(?P<msg_id>\d+)/results/$', 'results'),
)