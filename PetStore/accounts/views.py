from django.shortcuts import render,redirect
from accounts.models import Users,Profile_pictures
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password,check_password
from django.core.files.storage import FileSystemStorage



def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        city=request.POST['city']
        state=request.POST['state']
        address=request.POST['address']
        
        if confirm_password==password:
            if Users.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect('/accounts/register/')
            elif Users.objects.filter(mobile=mobile).exists():
                messages.info(request,'Mobile exists')
                return redirect('/accounts/register/')
            else:
                password=make_password(password)
                user=Users.objects.create(name=name,email=email,mobile=mobile,city=city,state=state,address=address,password=password)
                user.save()
                return redirect('/accounts/login/')  
        else:  
            messages.info(request,'Password and Confirm Password doesnt match')
            return redirect('/accounts/register/')
    return render(request,'cust_register.html')


def login(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        password=request.POST['password']
        try:
            user=Users.objects.get(mobile=mobile)
            if user.mobile==int(mobile) and check_password(password,user.password):
                request.session['id']=user.id
                return redirect('/profile/')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('/accounts/login/')            
        except ObjectDoesNotExist:
            messages.info(request,'Mobile doesnot exists')
            return redirect('/accounts/login/')    
    return render(request,'cust_login.html')


def logout(request):
    request.session.flush()
    return redirect('/accounts/login/')


def profile_pic(request, id):
    if request.method == "POST":
        profile_picture = request.FILES.get('profile_pic')  
        user_id = request.session.get('id')

        try:
            user = Users.objects.get(id=user_id)
            profile_pics, created = Profile_pictures.objects.get_or_create(user=user)
            profile_pics.profile_pic = profile_picture
            profile_pics.save()
        except Users.DoesNotExist:
            return redirect('/profile/')
    return redirect('/profile/')
