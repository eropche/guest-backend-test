import re
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import *
from ghuest_book.models import Message


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_class(self):
        return MessageSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return Response({"failed": "email"})
        username = request.data.get('username')
        if re.match('[!@#$]', username):
            return Response({"failed": "username"})
        text = request.data.get('text')
        
        message = Message()
        message = message.construct(username, email, text)
        message.save()

        return Response({"success": "true"})