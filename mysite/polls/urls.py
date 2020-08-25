

from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.default_page, name='default_page'),        
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^JsonList/', views.JsonListView.as_view(), name='JsonList'),
    
    url(r'^root/$', views.root_list, name='root'),
    url(r'^(?P<node_name>\S+)/children/$', views.node_list, name="node"),

]

