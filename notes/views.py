from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from .models import Note


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
                if title:
                    note = Note.objects.filter(
                        user = user[0],
                        title = title
                    )
                elif pk:
                    note = Note.objects.filter(
                        user = user[0],
                        pk = pk
                    )
                if note:
                    context = {
                        'title': note[0].title,
                        'datetime': note[0].datetime,
                        'content': note[0].content,
                        'type': note[0].type,
                        'pk': note[0].pk
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
                notes = Note.objects.filter(user=user[0])[::-1]
                context = {}
                for note in notes:
                    context[note.title] = {'content': note.content, 'datetime': note.datetime, 'pk': note.pk}
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
        noteType = request.POST.get('noteType')
        content = request.POST.get('content')
        if username and token and noteType and content:
            user = User.objects.filter(username=username, token=token)
            if user:
                user = uesr[0]
                if not Note.objects.filter(title=title):
                    if noteType in Note.allowed_types:
                        note = Note.objects.create(
                            title = title,
                            user = user,
                            content = content,
                        )
                        return JsonResponse({"Status": "FILE_CREATED", "pk": note.pk})
                    return JsonResponse({"Status": "ERR_TYPE_IS_INCORRECT"})
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
