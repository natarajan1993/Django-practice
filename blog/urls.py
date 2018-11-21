from django.urls import path
from . import views
from .views import (PostListView, PostDetailView,
					PostCreateView, PostUpdateView,
					PostDeleteView, UserPostListView)

urlpatterns = [
            path('',PostListView.as_view(), name = 'blog-home'), # Default naming convention for the CBV is <app>/<model>_<viewtype>.html
            path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'), # pk is primary key. So each url will contain a number corresponding to the post
            path('post/<str:username>/',UserPostListView.as_view(), name = 'user-posts'), # If the user goes to post/username, then call the UserPostListView view
			path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
			path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
			path('post/new/',PostCreateView.as_view(), name = 'post-create'),
            path('about/',views.about, name = 'blog-about'), 
]
