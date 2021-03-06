from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("create_new_entry/", views.create_new_entry, name='create_new_entry'),
    path(r'^edit/(?P<entry_title>\d+)/$', views.edit_entry_page, name='edit_entry'),
    path("<str:entry_title>", views.entry_page, name="entry_title"),
    path("random/", views.random_entry_page, name="random_entry_page"),
    path("search/", views.search_results_page, name='search_results'),
]
