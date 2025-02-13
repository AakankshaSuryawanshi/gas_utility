from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, service_request_list, register, user_login, user_logout

urlpatterns = [
    
    path('', home, name='home'),

    
    path('dashboard/', service_request_list, name='dashboard'),


    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
