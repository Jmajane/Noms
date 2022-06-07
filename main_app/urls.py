from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('meals/', views.MealList.as_view(), name="meal_list"),
    path('meals/new/', views.MealCreate.as_view(), name="meal_create"),
    path('meal/<int:pk>/', views.MealDetail.as_view(), name="meal_detail"),
    
]