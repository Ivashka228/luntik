from django.urls import include, path
from MyApp.views import index, pers, pers2, pers3

urlpatterns = [
    path('', index),
    path('pers', pers),
    path('pers2', pers2),
    path('pers3', pers3),
]