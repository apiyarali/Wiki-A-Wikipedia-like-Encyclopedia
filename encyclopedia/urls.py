from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage/", views.newpage, name="newpage"),
    path("wiki/<str:entry>", views.entrypage, name="entrypage"),
    path("search/", views.search, name="search"),
    path("random/", views.random, name="random"),
    path("edit/<str:edit_entry>", views.editpage, name="editpage")
]
