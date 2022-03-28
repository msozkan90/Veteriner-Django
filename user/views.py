from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from django.shortcuts import reverse


class UserCreateView(generic.CreateView):
	template_name = "register.html"
	form_class = CreateUserForm
	context_object_name = "owners"
	def get_success_url(self):
		return reverse("user:sign_in")
	def form_valid(self,form):
		form = CreateUserForm(self.request.POST)
		if  form.is_valid:
			forms = form.save(commit=False)
			forms.save()
			messages.success(self.request,"You registered successfully. Please login.")
			return super(UserCreateView, self).form_valid(form)			
	def form_invalid(self,form):
		form = CreateUserForm(self.request.POST)
		password1= form.data.get('password1')
		password2= form.data.get('password2')
		username= form.data.get('username')
		email = form.data.get('email')
		email_check=User.objects.filter(email=email)
		users=User.objects.filter(username=username)
		if(password1 != password2):
			messages.warning(self.request,"Passwords did not match")
			return super(UserCreateView, self).form_invalid(form)
		if(users):
			messages.warning(self.request,"This user name is already taken")
			return super(UserCreateView, self).form_invalid(form)
		if(email_check):
			messages.warning(self.request,"This email is already taken")
			return super(UserCreateView, self).form_invalid(form)

class UserLoginView(generic.FormView):
	template_name = "login.html"
	form_class = AuthenticationForm
	def get_success_url(self):
		return reverse("hayvanlar:index")
	def form_valid(self,form):
		form = AuthenticationForm(self.request.POST)
		username = self.request.POST.get('username')
		password =self.request.POST.get('password')
		user = authenticate(self.request, username=username, password=password)
		if  form.is_valid:
			login(self.request, user)
			messages.success(self.request, 'You logged in successfully')
			return super(UserLoginView, self).form_valid(form)	
	def form_invalid(self,form):
		form = AuthenticationForm(self.request.POST)
		username = self.request.POST.get('username')
		username_check=User.objects.filter(username=username)
		if(not username_check):
			messages.warning(self.request, 'Username incorrect ')
			return super(UserLoginView, self).form_invalid(form)
		else:
			messages.warning(self.request, 'Password incorrect ')
			return super(UserLoginView, self).form_invalid(form)
def sign_out(request):
	logout(request)
	messages.success(request, "You logged out successfully")
	return redirect("hayvanlar:index")




# def sign_in(request):
# 	form=AuthenticationForm()
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password =request.POST.get('password')

# 		user = authenticate(request, username=username, password=password)
# 		username_check=User.objects.filter(username=username)
# 		if user is not None:
# 			login(request, user)
# 			messages.success(request, 'You logged in successfully')
# 			return redirect('hayvanlar:index')
# 		elif(not username_check):
# 			messages.warning(request, 'Username incorrect ')
# 		else:
# 			messages.warning(request, 'Password incorrect ')
# 			context = {"form":form}
# 			return redirect('user:sign_in')
# 	context = {"form":form}
# 	return render(request, 'login.html', context)

# USER İŞLEMLERİ
# def register(request):
	
# 	form=CreateUserForm()
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		password1= form.data.get('password1')
# 		password2= form.data.get('password2')
# 		username= form.data.get('username')
# 		email = form.data.get('email')
# 		email_check=User.objects.filter(email=email)
# 		users=User.objects.filter(username=username)
# 		try:
# 			if form.is_valid:
# 					user = form.save(commit=False)
# 					user.save()
# 					messages.success(request,"You registered successfully. Please log in.")
# 					return redirect("user:sign_in")

# 		except(ValueError):
# 			if(password1 != password2):
# 					messages.warning(request,"Passwords did not match")
# 			if(users):
# 				messages.warning(request,"This user name is already taken")
# 			if(email_check):
# 					messages.warning(request,"This email is already taken")

# 			return redirect("user:register")
# 	return render(request,"register.html",{"form":form})

