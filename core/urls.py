from django.urls import path 
from . import views


urlpatterns = [
    path('time/' ,  views.time, name='time'),
    path('about/' , views.about , name = 'about'),
    path('' , views.index , name='index'),
    path('contact_us/', views.contact_us ,name='contacta_us'),
    path('my_account/' , views.my_account , name='my_account'),

    

]