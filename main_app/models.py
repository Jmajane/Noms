from django.db import models



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
    dish = models.CharField(max_length=10, choices=MEALS)
    Red_Meat = models.IntegerField()
    Fish_Chicken_Eggs = models.IntegerField()
    Nuts_Seeds_Beans_Tofu = models.IntegerField()
    Dairy = models.IntegerField()
    Vegetable = models.IntegerField()
    Fruits = models.IntegerField()
    Healthy_Fats_Oils = models.IntegerField()
    Whole_Grains = models.IntegerField()

    Sugary_Treats = models.IntegerField()
    Salty_Treats = models.IntegerField()
    Wheat_Flour_Corn_Treats = models.IntegerField()
    Alcohol = models.IntegerField()

    def __str__(self):
        return self.dish

    class Meta:
        ordering = ['dish']
