from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.urls import include

urlpatterns = [
        path('index/', views.index, name="index"),
        path('submit/', views.SubmitView, name="submit"),
	path('about/', views.about, name="about"),
]
