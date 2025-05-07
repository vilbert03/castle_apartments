from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='apartment-index'),
    path('<int:id>', views.get_apartment_by_id, name='apartment_by_id'),
]