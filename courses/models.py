from django.db import models

class Courses(models.Model):

    class CoursePeriod(models.IntegerChoices):
        THREE_MONTHS = 1, '3 Months'
        SIX_MONTHS = 2, '6 Months'
        NINE_MONTHS = 3, '9 Months'
        ONE_YEAR = 4, '1 Year'
        TWO_YEAR = 5, '2 Year'
        THREE_YEAR = 6, '3 Year'
        FOUR_YEAR = 7, '4 Year'
        FIVE_YEAR = 8, '5 Year'

    class Levels(models.IntegerChoices):
        BEGINNER = 1, 'Beginner'
        INTERMEDIATE = 2, 'Intermediate'
        ADVANCED = 3, 'Advanced'

    class Categories(models.IntegerChoices):
        WEB_DEVELOPMENT = 1, 'Web Development'
        DATA_SCIENCE_AI = 2, 'Data Science & AI'
        UI_UX_DESIGN = 3, 'UI/UX Design'
        CLOUD_AND_DEVOPS = 4, 'Cloud Engineering & DevOps'

    name = models.CharField(max_length=50)
    duration = models.IntegerField(choices=CoursePeriod.choices, default=CoursePeriod.ONE_YEAR)
    price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    description = models.TextField()
    level = models.IntegerField(choices=Levels.choices, default=Levels.BEGINNER)
    category = models.IntegerField(choices=Categories.choices, blank=False)
    thumbnail = models.ImageField(upload_to='courses/thumbnail', default='courses/thumbnail/default.jpg', blank=True, null=True)
    
    @property
    def actual_price(self):
        if self.discount>0:
            return (self.price*(100-self.discount))/100
        return self.price

    def __str__(self):
        return self.name