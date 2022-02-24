from django.db import models
from django.contrib.auth.models import User

class NoteBook(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}/{self.title}"

class Note(models.Model):
    title = models.CharField(max_length=24)
    notebook = models.ForeignKey(NoteBook, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noteType = models.CharField(max_length=24)
    datetime = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    allowed_types = ['note', 'kanban', 'table']
    def __str__(self):
        return f"{self.user}/{self.notebook.title}/{self.title}"
