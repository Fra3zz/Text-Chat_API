from django.urls import path
from  . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path('blogposts/edit/<int:pk>', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost_edit'),
    path("blogposts/search/", views.BlogPostList.as_view(), name = "title_view"),
]