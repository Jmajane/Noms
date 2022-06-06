from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



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

    def __str__(self):
        return self.dish

    class Meta:
        ordering = ['dish']
