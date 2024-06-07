from . import views
from django.urls import path

urlpatterns = [
    path("index/", views.index, name="index"),
    path("get/", views.home, name="get"),
    path("add/", views.add_food.as_view(), name="add"),
    path("tasks/", views.perform_task, name="tasks"),
    path("tasks1/", views.perform_task2, name="tasks1"),
    path("nosql/<int:idd>", views.get_data, name="nosql"),
]
