from django.urls import path
from . import views

app_name = 'buildTrain'

urlpatterns = [
    path('', views.home, name='home'),
    path('select_hand/', views.select_hand, name='hand'),
    path('select_station/', views.select_station, name='station'),
    path('build_train/<int:start>', views.build_train, name='build'),
]