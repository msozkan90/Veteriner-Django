from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages

# USER İŞLEMLERİ
def register(request):
	
	form=CreateUserForm()
	if request.method == 'POST':
		
		form = CreateUserForm(request.POST)
		password1= form.data.get('password1')
		password2= form.data.get('password2')
		username= form.data.get('username')
		email = form.data.get('email')
		email_check=User.objects.filter(email=email)
		users=User.objects.filter(username=username)
		try:
			if form.is_valid:
					user = form.save(commit=False)
					user.save()
					messages.success(request,"You registered successfully. Please log in.")
					return redirect("user:sign_in")

		except(ValueError):
			if(password1 != password2):
					messages.warning(request,"Passwords did not match")
			if(users):
				messages.warning(request,"This user name is already taken")
			if(email_check):
					messages.warning(request,"This email is already taken")

			return redirect("user:register")
	return render(request,"register.html",{"form":form})



def sign_in(request):
	form=AuthenticationForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		username_check=User.objects.filter(username=username)
		if user is not None:
			login(request, user)
			messages.success(request, 'You logged in successfully')
			return redirect('hayvanlar:index')
		elif(not username_check):
			messages.warning(request, 'Username incorrect ')
		else:
			messages.warning(request, 'Password incorrect ')
			context = {"form":form}
			return redirect('user:sign_in')
	context = {"form":form}
	return render(request, 'login.html', context)

def sign_out(request):
	logout(request)
	messages.success(request, "You logged out successfully")
	return redirect("hayvanlar:index")
