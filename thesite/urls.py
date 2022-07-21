from django.urls import path
#from . import views
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('', LandView.as_view(), name="land"),
    path('home', HomeView.as_view(), name="home"),
    path('browse_post/', BrowseView.as_view(), name="browse_post"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'), 
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('myideas/',MyIdeasView.as_view(),name='my_ideas'),
    path('collaborate/<int:post_id>/',request_collaborate,name='collaborate'),
    path('discussions/',discussion_lists,name='discussions'),
    path('messages/<int:disc_id>/',messages_details,name='messages'),
    path('connections/<int:post_id>/',connection_details,name='connections'),
]
