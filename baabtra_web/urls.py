from django.urls import path
from . import views


urlpatterns=[
    path('home',views.b_h),
    path('index',views.index)
   
]  
