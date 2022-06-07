from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('meals/', views.MealList.as_view(), name="meal_list"),
    path('meals/new/', views.MealCreate.as_view(), name="meal_create"),
    path('meal/<int:pk>/', views.MealDetail.as_view(), name="meal_detail"),
    path('meal/<int:pk>/update', views.MealUpdate.as_view(), name="meal_update"),
    path('meal/<int:pk>/delete', views.MealDelete.as_view(), name="meal_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('account/profile/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('account/profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),


]