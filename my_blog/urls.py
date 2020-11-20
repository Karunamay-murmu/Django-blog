from django.urls import path, include

from .views import (
    Home,
    CategoryPost,
    PostPageView,
    ContactFormView,
    EmailSubscription,
    AboutView,
    PrivacyPolicyView,
    TermsOfServiceView,
    Search
)
from .models import Post, Categorie, Comment
from write_blog.views import EditOrPublishDraft, EditOrSwitchPostToDraft

app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search', Search.as_view(), name='search'),
    path('category/<slug:slug>',
         CategoryPost.as_view(), name='category'),
    path('<slug:slug>',
         PostPageView.as_view(), name='post_detail'),
    path('post/<str:id>/<slug:slug>/edit-post',
         EditOrSwitchPostToDraft.as_view(), name='edit-post'),
    path('draft/<str:id>/edit-draft',
         EditOrPublishDraft.as_view(), name='edit-or-publish-draft'),
    path('report/', ContactFormView.as_view(), name='report'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('subscribe/', EmailSubscription.as_view(), name='subscribe'),
    path('about/', AboutView.as_view(), name='about'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms-of-service/', TermsOfServiceView.as_view(), name='terms'),
]
