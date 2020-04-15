from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('detail/',views.detail, name="detail"),
    path('signin/',views.signin, name="signin"),
    path('logout/',views.logout, name="logout"),
    path('delete/',views.delete, name="delete"),
    path('update/',views.update, name="update"),
]
