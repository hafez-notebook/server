from django.urls import path
from .views import newNoteView, editNoteView, deleteNoteView, getNoteView, getNotesView, getNotebookView, newNotebookView, deleteNotebookView

urlpatterns = [
    path('new/', newNoteView.as_view(), name="newNoteNote"),
    path('edit/', editNoteView.as_view(), name="editNoteView"),
    path('delete/', deleteNoteView.as_view(), name="deleteNoteView"),
    path('get/', getNoteView.as_view(), name="getNoteView"),
    path('getNotes/', getNotesView.as_view(), name="getNoteView"),
    path('newNotebook/', newNotebookView.as_view(), name="newNotebookView"),
    path('getNotebook/', getNotebookView.as_view(), name="getNotebookView"),
    path('deleteNotebook/', deleteNotebookView.as_view(), name="deleteNotebookView"),
]
