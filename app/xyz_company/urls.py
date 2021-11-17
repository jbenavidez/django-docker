from django.urls import path

from . import views

urlpatterns = [
            path('', views.Home, name='Home'),
            path('load-data/', views.dump_testing_data, name='dump_testing_data'),
 
        ]