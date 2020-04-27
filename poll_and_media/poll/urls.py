from django.urls import path
from . import views

app_name = "vote"

urlpatterns = [
    path('',views.index, name="index"),
    path('create/',views.create, name='create'),
    path('<int:vote_pk>/',views.detail, name='detail'),
    path('<int:vote_pk>/create_comment/',views.create_comment,name="create_comment")
]