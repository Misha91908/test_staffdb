from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^list/$', views.PersonListView.as_view(), name='list'),
    url(r'^person/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='person'),
    url(r'^alphabet/$', views.AlphabetListView.as_view(), name='alphabet'),
    url(r'^last_name/(?P<last_name>[-\w]+)$', views.AlphabetDetailView.as_view(), name='last_name'),
]