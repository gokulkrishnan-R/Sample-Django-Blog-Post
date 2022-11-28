from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField()
    author=models.TextField()
    image=models.ImageField(upload_to="images/", blank=True, null=True)
    posted_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['posted_on']

    def __unicode__(self): 
        return(self.title)
    class Meta:
        verbose_name_plural="Posts" #This will handle the extra "s" (singular or plural in models) 

#Creating profile model 
class Profile(models.Model):
    class Model:
        verbose_name_plural="Users"
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=120)
    comment_body=models.CharField(max_length=256)
    posted_on=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return('Comment {} by {}: '.format(self.comment_body, self.name))