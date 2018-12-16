from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = github
        fields = ['login','id','node_id','repos_url']