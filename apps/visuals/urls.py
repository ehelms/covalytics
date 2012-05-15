from django.conf.urls import patterns, include, url

urlpatterns = patterns('visuals',
    url(r'^$', 'views.home', name='home'),
)
