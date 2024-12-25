# DJANGO IMPORTS
from django.shortcuts import get_object_or_404

# REST FRAMEWORK IMPORTS
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# PROJECT IMPORTS
from .models import Articles, Comment
from .serializers import ArticleSerializer, CommentSerializer
from customUsers.permissions import IsAdmin

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def create_article(request):
    try:
        serializer = ArticleSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Article created successfully!", "article": serializer.data}, status=201)
        
        return Response(serializer.errors, status=400)
    except:
        return Response(
            {"message":"Something went wrong"},
            status = 500)
    
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdmin])  
def update_article(request, article_id):
    try:
        article = get_object_or_404(Articles, id=article_id)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Article updated successfully!", "article": serializer.data}, status=200)
        
        return Response(serializer.errors, status=400)
    except:
        return Response(
            {"message":"Something went wrong"},
            status = 500)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdmin])
def delete_article(request, article_id):
    try:
        article = get_object_or_404(Articles, id=article_id)
        article.delete()
        return Response({"message": "Article deleted successfully!"}, status=200)
    except:
        return Response(
            {"message":"Something went wrong"},
            status = 500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, article_id):

    article = get_object_or_404(Articles, id=article_id)
    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(author=request.user, article=article)
        return Response({
            "message": "Comment added successfully!",
            "comment": serializer.data
        }, status=201)
    
    return Response(serializer.errors, status=400)
