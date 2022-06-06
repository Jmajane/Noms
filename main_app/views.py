from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Meal


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class MealList(TemplateView):
    template_name = "meal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = Meal.objects.all()

        return context
