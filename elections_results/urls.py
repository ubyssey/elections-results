from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/', 'live_feed.views.results'),
    url(r'^up-next/', 'live_feed.views.up_next'),
    url(r'^call-race/', 'live_feed.views.call_race'),
)
