from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile/")
    name = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)


    def __str__(self):
        return str(self.user)


class Meal(models.Model):
    BREAKFAST = 'BREAKFAST'
    LUNCH = 'LUNCH'
    DINNER = 'DINNER'
    SNACKS = 'SNACKS'
    MEALS = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACKS, 'Snacks'),
    ]
    created_on = models.DateTimeField(auto_now_add=True)
    dish = models.CharField(max_length=10, choices=MEALS)
    Red_Meat = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Fish_Chicken_Eggs = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Nuts_Seeds_Beans_Tofu = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Dairy = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Vegetable = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Fruits = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Healthy_Fats_Oils = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Whole_Grains = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    Sugary_Treats = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Salty_Treats = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Wheat_Flour_Corn_Treats = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Alcohol = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.dish

    class Meta:
        ordering = ['dish']
