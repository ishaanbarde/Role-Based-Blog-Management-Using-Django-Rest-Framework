from rest_framework import serializers
from .models import Articles, Comment
from customUsers.serializers import custUser_Serialization

class ArticleSerializer(serializers.ModelSerializer):
    author = custUser_Serialization(read_only=True)
    
    class Meta:
        model = Articles
        fields = ['id', 'title', 'content', 'author', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user 
        validated_data['author'] = user
        return Articles.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = custUser_Serialization(read_only=True)

    class Meta:
        model   = Comment
        fields  = ['id', 'content', 'author', 'created_at'] 