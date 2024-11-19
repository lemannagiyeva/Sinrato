from django.urls import path

from . import views


urlpatterns = [
    path ('products/' , views.product , name='product'),
    path('shop/<int:pk>', views.shop , name='shop'),
]