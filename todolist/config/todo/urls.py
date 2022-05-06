from django.urls import path
from .views import TodoDetail, Todolist, TodoCreate, TodoUpdate, TodoDelete


urlpatterns = [
  path('', Todolist.as_view(), name="todo_list"),
  path('detail/<int:pk>', TodoDetail.as_view(), name="todo_detail"),
  path('create/', TodoCreate.as_view(), name="todo_create"),
  path('update/<int:pk>', TodoUpdate.as_view(), name="todo_update"),
  path('delete/<int:pk>', TodoDelete.as_view(), name="todo_delete"),
]
