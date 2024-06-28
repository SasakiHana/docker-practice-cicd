# urls.py

from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add, name="add"),
    path("update_task_complete/", mytodo.Update_Task_Complete, name="update_task_complete"),
    path("tasks/<int:task_id>/edit/", mytodo.edit, name="edit_task"),
    path("delete_task/", mytodo.delete_task, name="delete_task"),
    ]
