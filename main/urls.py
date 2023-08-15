from django.urls import path
from . import views

urlpatterns = [
    path('api/gigs/', views.GigView.as_view()),
    path('api/gigs/<int:pk>/', views.GigDetail.as_view())
]