from django.urls import path
from .views import ReserVeListView


app_name = 'store'

urlpatterns = [
  path('reserve_list', ReserVeListView.as_view(), 'reserve_list')
]
