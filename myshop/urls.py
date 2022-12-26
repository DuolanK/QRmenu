from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adm/', admin.site.urls),
    path('/', include('waiter.urls', namespace='waiter')),
    path('/', include('orders.urls', namespace='orders')),
    path('/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls', namespace='myshop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
