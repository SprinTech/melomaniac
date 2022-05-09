from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserList.as_view(), name="user-list"),
    path("<int:pk>/", views.UserDetail.as_view(), name='user-detail'),
    path("create/", views.UserCreate.as_view(), name='user-create'),
    path("<int:pk>/update/", views.UserUpdate.as_view(), name='user-update'),
    path("<int:pk>/delete/", views.UserDelete.as_view(), name='user-delete'),
]
