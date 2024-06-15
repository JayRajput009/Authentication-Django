from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# from authenticationapp.models import Authentication

# Create your views here.
def register(request):
    
    if request.method == "POST":
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        password  = data.get('password')



        user = User.objects.filter(username = username)

        if user.exists():
            
            return redirect('/')
        
        

        user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            username = username,
            password=  password
            )
        # user.set_password(password)
        # user.save()


        return redirect('/')    
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')