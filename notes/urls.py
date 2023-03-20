from django.urls import path
from .views import NotesHomePage, NotePage, NoteCreatePage, NoteUpdatePage, NoteDeletePage

urlpatterns = [
    path('', NotesHomePage.as_view(), name='home'),
    path('note/<int:pk>/', NotePage.as_view(), name="note-detail"),
    path('note/new/', NoteCreatePage.as_view(), name="note-create"),
    path('note/<int:pk>/update/', NoteUpdatePage.as_view(), name="note-update"),
    path('note/<int:pk>/delete/', NoteDeletePage.as_view(), name="note-delete"),
]
