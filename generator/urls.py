from django.urls import path
from generator.views import home, generate_password

urlpatterns = [
   
    path('', home, name='home'),
    path('password_generator', generate_password, name='generate_password')
]
