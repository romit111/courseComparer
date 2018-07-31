from django.contrib import admin
from django.urls import path,include
from course_compare import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('course_compare.urls')),
    path('',views.home,name='home'),
]
