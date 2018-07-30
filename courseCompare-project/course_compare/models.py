from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    difficulties = (
        ("beginner","beginner"),
        ("intermediate","intermediate"),
        ("advanced","advanced"),
    )
    title = models.CharField(max_length=254)
    short_description = models.TextField()
    pub_date = models.DateTimeField()
    instructor_name = models.CharField(max_length=254)
    ratings = models.DecimalField(max_digits=5,decimal_places=2)
    price = models.DecimalField(max_digits=7,decimal_places=2 )
    category = models.ManyToManyField(Subcategory)
    photo = models.ImageField(upload_to='images')
    duration = models.DecimalField(max_digits=7,decimal_places=3)
    certification = models.BooleanField(default=False)
    difficulty_level = models.CharField(max_length=50,choices=difficulties,default='Beginner')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    wishlist = models.ManyToManyField(Course,blank=True)
    full_name = models.CharField(max_length = 50,blank = True)
    country = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 10)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username



