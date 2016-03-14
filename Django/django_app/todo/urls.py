from django.conf.urls import url

from . import views

app_name = 'todo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^remove/$', views.remove_item, name='remove'),
    url(r'^complete/$', views.mark_complete, name='complete'),
]
