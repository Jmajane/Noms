from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from .models import Meal, Profile, FriendRequest, Friends1
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.contrib import messages
from .forms import createUserForm, profileForm


# def registerPage(request):
#     if request.method == 'POST':
#         form = createUserForm(request.POST)
#         profile_form = profileForm(request.POST)

#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             profile.save()

#             messages.success(request,  'Your account has been successfully created')

#             return redirect('login')
            
#     context = {'form': form, 'profile_form': profile_form}
#     return render(request, 'app_name/signup.html', context)



class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["friends"] = Friends1.objects.all()
        return context


class About(TemplateView):
    template_name = "about.html"


class MealCreate(CreateView):
    model = Meal
    fields = ['dish', 'Red_Meat', 'Fish_Chicken_Eggs', 'Nuts_Seeds_Beans_Tofu', 'Dairy', 
    'Vegetable', 'Fruits', 'Healthy_Fats_Oils', 'Whole_Grains', 'Sugary_Treats',
    'Salty_Treats', 'Wheat_Flour_Corn_Treats', 'Alcohol']
    template_name = "meal_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MealCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('meal_detail', kwargs={'pk': self.object.pk})


class MealDetail(DetailView):
    model = Meal
    template_name = "meal_detail.html"
    

class MealUpdate(UpdateView):
    model = Meal
    fields = ['dish', 'Red_Meat', 'Fish_Chicken_Eggs', 'Nuts_Seeds_Beans_Tofu', 'Dairy', 
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
            new_profile = Profile.objects.create(user=user)
            print(new_profile)
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

@method_decorator(login_required, name='dispatch')
class ProfileDetail(View):
    template_name = "profile_detail.html"
    def get(self, request, **kwargs):
        profile = Profile.objects.get(user=request.user)
        return render(request, self.template_name, {"profile":profile})

    # def friend_request(request, pk):
    #     sender = request.user
    #     recipient = User.objects.get(id=pk)
    #     model = FriendRequest.objects.get_or_create(sender=request.user, receivers=recipient)
    #     return redirect('/meals/')

    # def add_or_remove_friend(request, operation, pk):
    #     new_friend = User.objects.get(id=pk)
    #     if operation == 'add':
    #         fq = FriendRequest.objects.get(sender=new_friend, receivers=request.user)
    #         Friends1.make_friend(request.user, new_friend)
    #         Friends1.make_friend(new_friend, request.user)
    #         fq.delete()
    #     elif operation == 'remove':
    #         Friends1.lose_friend(request.user, new_friend)
    #         Friends1.lose_friend(new_friend, request.user)
    #     return redirect('form4')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     sender = self.request.user
    #     context["friends"] = sender.friends1_set.all()
    #     return context


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ('profile_pic', 'name', 'favorite_food', 'bio', 'workout_days')
    template_name = "profile_update.html"

    def get_success_url(self):
        return reverse('profile_detail')

class ProfileCreate(CreateView):
    model = Profile
    fields = ['profile_pic', 'name', 'favorite_food', 'bio', 'workout_days']
    template_name = "profile_create.html"

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["user"] = User.objects.get(id=self.request.user.id)
        return context

class FriendProfileAssoc(View):
    def get(self, request, pk, user_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Friends1.objects.get(pk=pk).user.remove(user_pk)
        if assoc == "add":
            Friends1.objects.get(pk=pk).user.add(user_pk)
        return redirect('home')





