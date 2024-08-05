from django.urls import path
from . import views

urlpatterns = [
    path('<str:table_name>/', views.table_view, name='table_view'),
]
