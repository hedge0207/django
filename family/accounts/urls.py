from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('singup/',views.signup,name="signup"),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<int:user_pk>/profile/',views.profile,name='profile'),
    path('<int:user_pk>/user_delete/',views.user_delete,name='user_delete'),
    path('user_update/',views.user_update,name='user_update'),
    ]