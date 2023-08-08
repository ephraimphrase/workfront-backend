from django.urls import path
from . import views

urlpatterns = [
    path('api/gigs/', views.GigsList.as_view()),
    path('api/gigs/<int:pk>/', views.GigDetails.as_view())
]