from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Articles, Comment
from customUsers.models import CustomUser

class ArticleTests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_user(username="admin", password="adminpass", role="Admin")
        self.client.force_authenticate(user=self.admin)
    
    def test_create_article(self):
        url = reverse('create_article')
        data = {
            "title": "Test Article",
            "content": "This is a test article."
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_article(self):
        article = Articles.objects.create(title="Old Title", content="Old Content", author=self.admin)
        url = reverse('update_article', kwargs={'article_id': article.id})
        data = {"title": "New Title", "content": "Updated Content"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        article = Articles.objects.create(title="Delete Me", content="To be deleted", author=self.admin)
        url = reverse('delete_article', kwargs={'article_id': article.id}) 
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="member", password="memberpass", role="Member")
        self.article = Articles.objects.create(title="Article for Comments", content="Content", author=self.user)
        self.client.force_authenticate(user=self.user)

    def test_add_comment(self):
        url = reverse('add_comment', kwargs={'article_id': self.article.id})  # /articles/comments/<article_id>/add/
        data = {"content": "This is a comment"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_list_comments(self):
    #     Comment.objects.create(content="First Comment", author=self.user, article=self.article)
    #     url = reverse('list_comments', kwargs={'article_id': self.article.id})  # /articles/comments/<article_id>/
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
