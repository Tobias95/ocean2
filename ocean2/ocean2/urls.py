from django.conf.urls import patterns, url

from theme import views

urlpatterns = patterns('',
    url(r'^$', views.frontpage, name='frontpage'),
    url(r'^$', include('theme.urls')),
    url(r'^useraccounts/', include('useraccounts.urls')),
)
