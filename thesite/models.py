from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField



#class Occupation(models.Model):
    #name = models.CharField(max_length=255)

    #def __str__(self):
    #    return self.name

    #def get_absolute_url(self):
    #    return reverse('home')

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Occupation(models.Model):
    occupation_name = models.CharField(max_length=200,default='')
    created_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.occupation_name

class Position(models.Model):
    name = models.CharField(max_length=200,default='')
    created_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField() 
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    interest = models.CharField(max_length=255, default = "Uncategorized")
    interest2 = models.CharField(max_length=255, default = "Uncategorized")
    interest3 = models.CharField(max_length=255, default = "Uncategorized")
    occupation = models.CharField(max_length=255, default = "Unemployed")

    #add more fields like tags and jobs here for user(acessed by user.profile.tags, etc.)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')





class Post(models.Model):

    

    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default = "Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    size = models.IntegerField()
    budget = models.IntegerField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default = "Uncategorized")
    category2 = models.CharField(max_length=255, default = "Uncategorized")
    category3 = models.CharField(max_length=255, default = "Uncategorized")
    position = models.CharField(max_length=255, default = "Uncategorized")
    position2 = models.CharField(max_length=255, default = "Uncategorized")
    position3 = models.CharField(max_length=255, default = "Uncategorized")

    snippet = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    terms = models.IntegerField(null=True)
    #images

    image_1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image_3 = models.ImageField(null=True, blank=True, upload_to="images/")
    #make sure to migrate

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    message = models.TextField()
    created_date = models.DateTimeField(default=datetime.today)

class Discussion(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    messages = models.ManyToManyField(Message)