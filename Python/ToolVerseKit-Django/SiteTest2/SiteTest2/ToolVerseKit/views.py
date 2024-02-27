from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
import random , string
from django.core.mail import send_mail
from django.db import connection
def homePage(request):
    if request.user.is_authenticated:
        return redirect('home', username=request.user.username)
    return render(request, 'ToolVerseKit/home.html')
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home', username=request.user.username)
    return render(request, 'ToolVerseKit/signup.html')
def recoverPasswordPage(request):
    if request.user.is_authenticated:
        return redirect('home', username=request.user.username)
    return render(request, 'ToolVerseKit/recoverpassword.html')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home', username=request.user.username)
    return render(request, 'ToolVerseKit/login.html')
def homePageLogged(request, username):
    if request.user.username == username:
        return render(request, 'ToolVerseKit/homeLogged.html', {'username': username})
    else:
        return redirect('home')
def profilePage(request, username):
    if request.user.username == username:
        return render(request, 'ToolVerseKit/profile.html', {'username': username})
    else:
        return redirect('home')
def signUpfunction(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstNameCreate')
        lastName = request.POST.get('lastNameCreate')
        username = request.POST.get('userCreate')
        email = request.POST.get('emailCreate')
        password = request.POST.get('passwordCreate')
        if username == '' or email == '' or password == '' or firstName == '' or lastName == '':
            return JsonResponse({'error': 'You need to complete all fields .'})
        elif User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists .'})
        hashed_password = make_password(password)
        account = User(username = username, email = email, password = hashed_password , last_name = lastName , first_name = firstName)
        account.save()
        with connection.cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE toolversekit.accountManager{username} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    SiteApp VARCHAR(255),
                    Username VARCHAR(255),
                    Password VARCHAR(255)
                );
            """)
        send_mail(subject = 'Account created' , message = f'Your account was created !\nUsername : {username}\nPassword : {password}' , from_email = 'ToolVerseKit@gmail.com' , recipient_list = [email])
        return JsonResponse({'success': 'Account created .'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
def recoverPasswordFunction(request):
    if request.method == 'POST':
        username = request.POST.get('userRecover')
        email = request.POST.get('emailRecover')
        if username == '' or email == '':
            return JsonResponse({'error': 'You need to complete all fields.'})
        else:
            users = User.objects.filter(username=username, email = email)
            if users.exists():
                user = users.first()
                new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
                user.set_password(make_password(new_password))
                user.save()
                send_mail(subject = 'Password reseted' , message = f'Your password for username : {username} was reseted .\nYour new password is : {new_password}' , from_email = 'ToolVerseKit@gmail.com' , recipient_list = [email])
                return JsonResponse({'success': 'Password changed successfully .'})
            else:
                return JsonResponse({'error': 'User or email incorrect .'})

    else:
        return JsonResponse({'error': 'Invalid request method'})
def loginFunction(request):
    if request.method == 'POST':
        username = request.POST.get('userLogin')
        password = request.POST.get('passwordLogin')
        if not username or not password:
            return JsonResponse({'error' : 'You need to complete all fields.'})
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': 'Logged.', 'username': user.username})
        else:
            return JsonResponse({'error' : 'User or email incorrect .'})
    else:
        return JsonResponse({'error' : 'Invalid request method.'})
def logoutFunction(request):
    logout(request)
    return redirect('home')