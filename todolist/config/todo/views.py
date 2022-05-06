from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
  ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Todo



class Todolist(ListView):
  model = Todo
  context_object_name = 'tasks'


class TodoDetail(DetailView):
  model = Todo
  context_object_name = 'task'


class TodoCreate(CreateView):
  model = Todo
  fields = "__all__"
  template_name = 'todo/todo_create.html'
  success_url = reverse_lazy('todo_list')


class TodoUpdate(UpdateView):
  model = Todo
  fields  = "__all__"
  template_name = 'todo/todo_update.html'
  success_url = reverse_lazy('todo_list')


class TodoDelete(DeleteView):
  model = Todo
  context_object_name = 'task'
  success_url = reverse_lazy('todo_list')
