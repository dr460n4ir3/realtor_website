from django.shortcuts import render
from .models import User

# Create your views here.
def registered_list(request):
    users = User.objects.all() # This will get all the users from the database
    # context is a dictionary that will be passed to the template
    context = {
        'users': users
    }
    return render(request, 'userreg.html', context) # This will pass the userreg

def registered_retrieve(request, pk):
    user = User.objects.get(id=pk) # This will get the specific user from the database
    context = {
        'user': user
    }
    return render(request, 'user.html', context)