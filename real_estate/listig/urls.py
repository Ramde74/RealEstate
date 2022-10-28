from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('',listing_list),
    path('listings/<pk>/',listing_retrieve),
    path('add-list',listing_create),
    path('listings/<pk>/edit',listing_update),
    path('listings/<pk>/delete',listing_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)