from django.db import models
from customUsers.models import CustomUser

class Articles(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    author      = models.ForeignKey(CustomUser,on_delete= models.CASCADE, related_name="articles")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content     = models.TextField()
    article     = models.ForeignKey(Articles, on_delete= models.CASCADE, related_name= "comments")
    author      = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name="comments")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"