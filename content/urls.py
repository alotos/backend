from django.urls import path
from . import views

urlpatterns = [
    path('cont/', views.content, name="content"),
]