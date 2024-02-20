from django.urls import path
from . import views

urlpatterns = [
    path('',views.home2,name='home2'),
    path('user_login/',views.user_login,name='user_login'),
    # path('logout/', views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('homee/',views.homee,name="homee")
    # Add more URL patterns as needed
]