from django.conf.urls import patterns, include, url

urlpatterns = patterns('reports',
    url(r'^reports/$', 'views.index', name='index'),
)
