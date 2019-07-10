from rest_framework import serializers
from ghuest_book.models import Message


class MessageSerializer(serializers.ModelSerializer):
   class Meta:
       model = Message
       fields = [
           'id',
           'username',
           'email',
           'created_at',
           'text'
       ]