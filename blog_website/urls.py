from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from my_blog.views import AboutView, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('registration.urls')),
    path('profile/', include('user_profile.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('my_blog.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404
handler500 = handler500
