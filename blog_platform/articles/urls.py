from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_article, name='create_article'),
    path('<int:article_id>/update/', views.update_article, name='update_article'),
    path('<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('comments/<int:article_id>/add/', views.add_comment, name='add_comment'),
]
