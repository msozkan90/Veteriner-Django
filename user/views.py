from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
# USER İŞLEMLERİ
def register(request):
	
	form=CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		try:
			if form.is_valid:
				user = form.save(commit=False)
				user.save()
				messages.success(request,"You registered successfully. Please log in.")
				return redirect("user:sign_in")
		except(ValueError):
			messages.warning(request,"Please fill the form correctly")
			return redirect("user:register")
	return render(request,"register.html",{"form":form})



def sign_in(request):
	form=AuthenticationForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, 'You logged in successfully')
			return redirect('hayvanlar:index')
		else:
			messages.warning(request, 'Username  or password is wrong ')
			context = {"form":form}
			return redirect('user:sign_in')
	context = {"form":form}
	return render(request, 'login.html', context)

def sign_out(request):
	logout(request)
	messages.success(request, "You logged out successfully")
	return redirect("hayvanlar:index")
