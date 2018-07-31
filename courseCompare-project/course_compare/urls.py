from django.urls import path,include
from . import views


urlpatterns = [
    path('scraping_test',views.scraping_test,name="scraping_test"),
    path('signup',views.signup,name='signup'),
]
