from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Meal
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class MealList(TemplateView):
    template_name = "meal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.request.GET.get('dish')

        if dish != None:
            context["meals"] = Meal.objects.filter(name_icontains=dish)
            context["header"] = f"Searching for {dish}"
        else:
            context["meals"] = Meal.objects.all()
            context["header"] = "Past Meals"
        return context

class MealCreate(CreateView):
    model = Meal
    fields = ['dish', 'Fish_Chicken_Eggs', 'Nuts_Seeds_Beans_Tofu', 'Dairy', 
    'Vegetable', 'Fruits', 'Healthy_Fats_Oils', 'Whole_Grains', 'Sugary_Treats',
    'Salty_Treats', 'Wheat_Flour_Corn_Treats', 'Alcohol']
    template_name = "meal_create.html"
    
    def get_success_url(self):
        return reverse('meal_detail', kwargs={'pk': self.object.pk})


class MealDetail(DetailView):
    model = Meal
    template_name = "meal_detail.html"
    

class MealUpdate(UpdateView):
    model = Meal
    fields = ['dish', 'Fish_Chicken_Eggs', 'Nuts_Seeds_Beans_Tofu', 'Dairy', 
    'Vegetable', 'Fruits', 'Healthy_Fats_Oils', 'Whole_Grains', 'Sugary_Treats',
    'Salty_Treats', 'Wheat_Flour_Corn_Treats', 'Alcohol']
    template_name = "meal_update.html"
    
    def get_success_url(self):
        return reverse('meal_detail', kwargs={'pk': self.object.pk})