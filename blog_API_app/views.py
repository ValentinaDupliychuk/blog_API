from rest_framework.views import APIView
from .models import BLOGS
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from blog.models import Note
from . import serializers


class BlogAPIView(APIView):
    def get(self, request):
        return Response(data=BLOGS)

    def post(self, request):
        pass


class NoteListCreateAPIView(APIView):
    def get(self, request: Request):
        objects = Note.objects.all()
        return Response([serializers.note_to_json(obj) for obj in objects])

    def post(self, request):
        data = request.data
        note = Note(**data)
        note.save(force_insert=True)

        return Response(
            serializers.note_created(note),
            status=status.HTTP_201_CREATED
        )

class NoteDetailedAPIView(APIView):
    def get(self, request, pk):
       note = get_object_or_404(Note, pk=pk)
       return Response(serializers.note_to_json(note))

    def put(self, request, pk):
        data = request.data(pk=pk)
        note = Note(**data)
        note.save(force_update=True)

        return Response(serializers.note_created(note))
