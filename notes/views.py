from django.shortcuts import render
from .models import Note
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

''' my function based view for Home Page
@login_required
def Home(request):
    user_notes = {
        'notes':Note.objects.filter(author=request.user)
    }
    return render(request, 'notes/home.html', user_notes)
'''

''' my function based view for Note details(detail Page)
@login_required
def Note_detail(request, pk):
    user_notes = {
        'note':Note.objects.get(id=pk)
    }
    return render(request, 'notes/note_detail.html', user_notes)
'''

class NotesHomePage(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-date_posted']
    paginate_by = 10
    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    
class NotePage(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    
class NoteCreatePage(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'memory']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NoteUpdatePage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'memory']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

class NoteDeletePage(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Note
    success_url = "/"
    
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False