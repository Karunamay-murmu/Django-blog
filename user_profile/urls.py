from django.urls import path, include

from .views import (
    Dashboard,
    Posts,
    Drafts,
    Comments,
    EditProfile,
    ProfileInfo,
    Search
)

app_name = 'dashboard'

urlpatterns = [
    path('<str:user>/<str:id>/',
         ProfileInfo.as_view(), name='profileInfo'),
    path('<str:user>/<str:id>/posts',
         Posts.as_view(), name='posts'),
    path('<str:user>/<str:id>/drafts',
         Drafts.as_view(), name='drafts'),
    path('<str:user>/<str:id>/comments',
         Comments.as_view(), name='comments'),
    path('<str:user>/<str:id>/edit-profile',
         EditProfile.as_view(), name='editProfile'),
    path('<str:user>/<str:id>/search',
         Search.as_view(), name='search'),
    path('<str:user>/<str:id>/', include('write_blog.urls'))
]
