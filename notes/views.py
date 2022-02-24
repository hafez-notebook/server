from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from .models import NoteBook, Note


@method_decorator(csrf_exempt, name="dispatch")
class getNotebookView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get("username")
        token = request.POST.get("token")
        title = request.POST.get("title")
        pk = request.POST.get("pk")

        if username and token:
            user = User.objects.filter(username=username, token_token=token)
            if user:
                user = user[0]
                if title:
                    notebook = NoteBook.objects.filter(user=user, title=title)
                elif pk:
                    notebook = NoteBook.objects.filter(user=user, pk=pk)
                else:
                    return JsonResponse({"Status": "ERR_ARGS"})
                if notebook:
                    notebook = notebook[0]
                    notebookNotes = Note.objects.filter(notebook=notebook)
                    context = {
                        "title": notebook.title,
                        "pk": notebook.pk,
                        "notes": notebookNotes
                    }
                    return JsonResponse({"Status": "SUCCESSED", "notebook": context})
                return JsonResponse({"Status": "ERR_NOTEBOOK_NOT_FOUND"})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_ARGS"})

@method_decorator(csrf_exempt, name="dispatch")
class newNotebookView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        title = request.POST.get('title')

        if username and token and title:
            user = User.objects.filter(username=username, token=token__token)
            if user:
                user = user[0]
                if not NoteBook.objects.filter(title=title):
                    NoteBook.objects.create(title=title, user=user)
                    return JsonResponse({"Status": "SUCCESSED"})
                return JsonResponse({"Status": "ERR_NOTEBOOK_EXISTS"})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_ARGS"})

@method_decorator(csrf_exempt, name="dispatch")
class deleteNotebookView(View):
    
    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        title = request.POST.get('title')

        if username and token and title:
            user = User.objects.filter(username=username, token__token=token)
            if user:
                user = user[0]
                notebook = NoteBook.objects.filter(user=user, title=title)
                if notebook:
                    notebook = notebook[0]
                    notes = Note.objects.filter(user=user, notebook=notebook)
                    notes.delete()
                    notebook.delete()
                    return JsonResponse({"Status": "SUCCESSED"})
                return JsonResponse({"Status": "ERR_NOTEBOOK_NOT_EXISTS"})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_ARGS"})

@method_decorator(csrf_exempt, name="dispatch")
class getNoteView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        title = request.POST.get('title')
        pk = request.POST.get('pk')

        if username and token:
            user = User.objects.filter(username=username, token__token=token)
            if user:
                user = user[0]
                if title:
                    note = Note.objects.filter(
                        user = user,
                        title = title
                    )
                elif pk:
                    note = Note.objects.filter(
                        user = user,
                        pk = pk
                    )
                if note:
                    note = note[0]
                    context = {
                        'title': note.title,
                        'notebook': note.notebook,
                        'datetime': note.datetime,
                        'content': note.content,
                        'type': note.type,
                        'pk': note.pk
                    }
                    return JsonResponse({"Status": "SUCCESSED", 'note': context})
                return JsonResponse({"Status": "NOTE_IS_NOTE_DEFIND"})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_ARGS"})


@method_decorator(csrf_exempt, name="dispatch")
class getNotesView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        if username and token:
            user = User.objects.filter(username=username, token__token=token)
            if user:
                user = user[0]
                notebooks = NoteBook.objects.filter(user=user)
                context = {}
                for notebook in notebooks:
                    notes = Note.objects.filter(user=user, notebook=notebook)
                    notesList = {}
                    for note in notes:
                        notesList[note.title] = {'pk': note.pk, 'datetime': note.datetime}
                    context[notebook.title] = notesList
                return JsonResponse({"Status": "SUCCESSED", "notes": context})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_ARGS"})

@method_decorator(csrf_exempt, name="dispatch")
class newNoteView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        title = request.POST.get('title')
        notebook = request.POST.get('notebook')
        noteType = request.POST.get('noteType')
        content = request.POST.get('content')
        if username and token and title and notebook and noteType and content:
            user = User.objects.filter(username=username, token=token)
            if user:
                user = uesr[0]
                if not Note.objects.filter(title=title):
                    notebook = NoteBook.objects.filter(user=user, title=notebook)
                    if notebook:
                        notebook = notebook[0]
                        if noteType in Note.allowed_types:
                            note = Note.objects.create(
                                title = title,
                                user = user,
                                notebook = notebook,
                                content = content,
                            )
                            return JsonResponse({"Status": "FILE_CREATED", "pk": note.pk})
                        return JsonResponse({"Status": "ERR_TYPE_IS_INCORRECT"})
                    return JsonResponse({"Status": "ERR_NOTEBOOK_NOT_EXISTS"})
                return JsonResponse({"Status": "ERR_TITLE_EXISTS"})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_LOW_ARGS"})


@method_decorator(csrf_exempt, name="dispatch")
class editNoteView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        pk = request.POST.get('pk')
        content = request.POST.get('content')
        title = request.POST.get('title')

        if username and token and pk and content and title:
            user = User.objects.filter(username=username, token=token)
            if user:
                note = Note.objects.filter(user=user, pk=pk)
                if note:
                    note = note[0]
                    note.title = title
                    note.content = content
                    note.save()
                    return JsonResponse({"Status": "NOTE_EDITED"})
                    return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
                return JsonResponse({"Status": "NOTE_NOT_EXISTS"})
        return JsonResponse({"Status": "ERR_ARGS"})


@method_decorator(csrf_exempt, name="dispatch")
class deleteNoteView(View):

    def get(self, request):
        return JsonResponse({"Status": "ERR_REQUEST_TYPE_IS_GET"})

    def post(self, request):
        username = request.POST.get('username')
        token = request.POST.get('token')
        pk = request.POST.get('pk')
        if username and token and pk:
            user = User.objects.filter(username=username, token=token)
            if user:
                user = user[0]
                note = Note.objects.filter(
                    user = user,
                    pk = pk
                )
                if note:
                    note.delete()
                    return JsonResponse({"Status": "NOTE_DELETED"})
                return JsonResponse({"Status": "NOTE_NOT_EXISTS"})
            return JsonResponse({"Status": "AUTHENTICATION_FAILED"})
        return JsonResponse({"Status": "ERR_ARGS"})
