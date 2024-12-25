from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('owner/createUser/', views.createUser,name='createUser'),
    path('owner/<int:user_id>/updateRole/', views.update_role,name='updateRole'),
    path('userlist/', views.list_users,name='userlist'),
]