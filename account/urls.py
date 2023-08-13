from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),
    path('accounts/login/', views.CustomTokenPairView.as_view()),
    path('accounts/refresh/', views.CustomTokenRefreshView.as_view()),
    path('api/sign-up', views.SignUpView.as_view()),
]