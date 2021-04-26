# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.contrib.auth.models import User,auth
# from django.contrib import messages
# from django.contrib.auth import get_user_model
# User = get_user_model()

# # Create your views here.
# def showDemoPage(request):
#     return render(request,"demo.html")

# def register(request): 
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         codechef_id = request.POST['codechef_id']
#         email = request.POST['email']
#         prn = request.POST['prn']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         user = User.objects.create_user(username = username,codechef_id=codechef_id,password=password1,email=email,first_name=first_name,last_name=last_name,prn=prn)
#         user.save();
#         print('User created')
#         return redirect('/')

#     else:
#         return render(request,"register.html")




from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def showDemoPage(request):
    return render(request,"demo.html")

def register(request): 
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        codechef_id = request.POST['codechef_id']
        email = request.POST['email']
        prn = request.POST['prn']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect("register")


            else:
                user = User.objects.create_user(username=username ,codechef_id=codechef_id,password=password1,email=email,first_name=first_name,last_name=last_name,prn=prn)
                user.save();
                print('User created')
                return redirect('login')

        else:
            messages.info(request,"Password not Macthing...")
            return redirect('register')
        return redirect('/')

    else:
        return render(request,"register.html")






# def register(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         codechef_id = request.POST['codechef_id']
#         email = request.POST['email']
#         prn = request.POST['prn']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username Taken')
#                 return redirect("register")

#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Email Taken')
#                 return redirect("register")


#             else:
#                 user = User.objects.create_user(username=username ,codechef_id=codechef_id,password=password1,email=email,first_name=first_name,last_name=last_name,prn=prn)
#                 user.save();
#                 print('User created')
#                 return redirect('login')

#         else:
#             messages.info(request,"Password not Macthing...")
#             return redirect('register')
#         return redirect('/')

#     else:
#         return render(request,"register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
<<<<<<< HEAD
            return redirect("/")
=======
            return redirect("events")
>>>>>>> 5163974 (Second commit-webpages liked...card removed.Event page added!)
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
<<<<<<< HEAD
    return redirect("/")
=======
    return redirect("/")



def events(request):
    return render(request,"events.html")
>>>>>>> 5163974 (Second commit-webpages liked...card removed.Event page added!)
