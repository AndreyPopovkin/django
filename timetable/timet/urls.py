
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.deadlines, name='deadlines'),
    url(r'^achieved/$', views.achieved, name='achieved'),
    url(r'^newTicketForm/$', views.newTicketForm, name='newTicketForm')
]