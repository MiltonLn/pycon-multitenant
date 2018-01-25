from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import Note


class NotesHome(TemplateView):
    template_name = 'notes/notes_home.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['notes'] = Note.objects.all()
        return context


class NoteCreateView(CreateView):
    model = Note
    fields = ['content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('home')
