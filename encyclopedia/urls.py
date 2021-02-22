from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_title>", views.entry_page, name="entry_title"),
    path("search/", views.search_results_page, name='search_results')
]
