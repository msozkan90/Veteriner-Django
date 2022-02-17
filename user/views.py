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
				messages.success(request,"Başarılı Bir Şekilde Kayıt Oldunuz")
				return redirect("user:sign_in")
		except(ValueError):
			messages.warning(request,"Lütfen Formu Kriterlere Uygun Doldurunuz.")
			return redirect("hayvanlar:animals")
	return render(request,"register.html",{"form":form})



def sign_in(request):
	form=AuthenticationForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, 'Oturum Açma İşlemi Başarılı')
			return redirect('hayvanlar:animals')
		else:
			messages.info(request, 'Kullanıcı adı  veya şifre hatalı ')

		context = {"form":form}
	
		return render(request, 'hayvanlar:animals', context)
	context = {"form":form}
	return render(request, 'login.html', context)

def sign_out(request):
	logout(request)
	messages.success(request, "Oturum Başarılı Bir Şekilde Kapatıldı")
	return redirect("hayvanlar:animals")
