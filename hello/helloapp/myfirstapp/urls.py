from django.conf.urls import url
from myfirstapp import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
]