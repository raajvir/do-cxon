from django.contrib import admin
from .models import Discussion, Position, Post, Category, Profile, Occupation

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Occupation)
admin.site.register(Position)
admin.site.register(Discussion)