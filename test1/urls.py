#
from django.urls import path
from test1 import views

app_name = 'test1'
urlpatterns = [
    path('predict_input/', views.predict_input, name='predict_input'),
    path('predict/', views.predict, name='predict'),
]
