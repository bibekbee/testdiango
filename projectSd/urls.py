from django.urls import path
from . import views


urlpatterns = [
    path('so/', views.someS),
    path('lo/', views.say_hello),
    path('home/', views.Home)
]
