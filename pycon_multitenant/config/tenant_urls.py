from django.urls import include, path
from notes.views import NotesHome


urlpatterns = [
    path('', NotesHome.as_view(), name='home'),
    path('notes/', include('notes.urls', namespace='notes')),
]
