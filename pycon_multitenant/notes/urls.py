from django.urls import path

from . import views


app_name = 'notes'

urlpatterns = [
    path('create/', views.NoteCreateView.as_view(), name='create')
]
