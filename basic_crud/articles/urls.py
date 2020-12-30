from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('create', views.article_create),
    path('<int:article_pk>/update', views.article_update),
    path('<int:article_pk>/delete', views.article_delete),
]
