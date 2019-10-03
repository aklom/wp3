from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('result', views.testresult, name="testresult"),
    path('aboutus', views.aboutus, name="aboutus"),

]