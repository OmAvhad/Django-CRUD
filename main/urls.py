from django.contrib import admin
from django.urls import path
from . import views
app_name  = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path("create", views.AuthorCreateView.as_view(), name="create"),
    path("<pk>/update", views.AuthorUpdateView.as_view(), name="update"),
    path("<pk>/delete", views.AuthorDeleteView.as_view(), name="delete"),
]
