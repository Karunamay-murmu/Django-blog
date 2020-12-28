from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from my_blog.views import AboutView, handler404, handler500
from write_blog.views import image_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('registration.urls')),
    path('profile/', include('user_profile.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('media/images/uploads/', csrf_exempt(image_upload)),
    path('', include('my_blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = handler404
handler500 = handler500
