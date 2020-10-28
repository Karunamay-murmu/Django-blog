from django.urls import path

# from .views import writePost
from .views import CreatePost

app_name = 'write_blog'

urlpatterns = [
    path('write-post/', CreatePost.as_view(), name='write_post')
]
