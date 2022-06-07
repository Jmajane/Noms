from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Meal, Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
            context["meals"] = Meal.objects.filter(name_icontains=dish, 
            user=self.request.user)
            context["header"] = f"Searching for {dish}"
        else:
            context["meals"] = Meal.objects.filter(user=self.request.user)
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


class MealDelete(DeleteView):
    model = Meal
    template_name = "meal_delete_confirmation.html"
    success_url = "/meals/"


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("meal_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


@method_decorator(login_required, name='dispatch')
class MealList(TemplateView):
    template_name = "meal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.request.GET.get("dish")
        if dish != None:
            context["meals"] = Meal.objects.filter(name_icontains=dish, 
            user=self.request.user)
            context["header"] = f"Searching for {dish}"
        else:
            context["meals"] = Meal.objects.filter(user=self.request.user)
            context["header"] = "Past Meals"
        return context

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"

