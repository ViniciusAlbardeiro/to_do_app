from django.urls import path
from . import views

urlpatterns = [path("", views.pagInit, name="pagInit")]
