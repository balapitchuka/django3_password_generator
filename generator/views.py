from django.shortcuts import render
import string
import random

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'generator/home.html', {})

def generate_password(request):
    """
    
    """
    if request.method == 'GET':
        characters_string = ''
        password = ''

        length = int(request.GET.get('length'))
        if request.GET.get('lowercase'):
            characters_string += string.ascii_lowercase
            password += random.SystemRandom().choice(string.ascii_lowercase)
        if request.GET.get('uppercase'):
            characters_string += string.ascii_uppercase
            password += random.SystemRandom().choice(string.ascii_uppercase)
        if request.GET.get('number'):
            characters_string += string.digits
            password += random.SystemRandom().choice(string.digits)
        if request.GET.get('special_character'):
            special_character = '!@#$%^&*()'
            characters_string += special_character
            password += random.SystemRandom().choice(special_character)
        
        remain_length = length - len(password)
        for index in range(remain_length):
            password += random.SystemRandom().choice(characters_string)

        # shuffle the array to distort and randomize the password
        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return render(request, 'generator/password.html', {'password' : password})

        

        
        