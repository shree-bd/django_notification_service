# Project hosted at https://github.com/shree-bd/Django_NotificationAPI

from django.contrib import admin
from django.urls import path
from notifications.views import create_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/transactions/', create_transaction, name='create_transaction'),
]
