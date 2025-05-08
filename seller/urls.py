from django.urls import path

from . import views

urlpatterns = [
    # http: //localhost:9000/seller
    path('', views.index, name='seller-index'),
]


