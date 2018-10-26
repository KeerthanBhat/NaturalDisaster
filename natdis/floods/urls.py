from django.conf.urls import url
from floods import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^predict/$', views.predict, name='predict'),
	url(r'^manage/$', views.manage, name='manage'),
]