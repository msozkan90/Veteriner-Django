
from django.shortcuts import render,redirect,get_object_or_404
from .forms import SahipForm,HayvanForm
from hayvanlar.models import Hayvan,HayvanSahibi
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"index.html")

@login_required(login_url = "user:sign_in")
def hayvanlar(request):
    query=request.GET.get('search')
    hayvanlar=Hayvan.objects.all()
    form=HayvanForm()
    if request.method == 'POST':
        form = HayvanForm(request.POST)
        try:
            if form.is_valid:
                hayvan_ = form.save(commit=False)
                hayvan_.save()
                messages.success(request,"Hayvan Başarılı Bir Şekilde Eklendi")
                return redirect("hayvanlar:animals")
        except(ValueError):
                messages.warning(request,"Lütfen Formu Uygun Bir Şekilde Doldurun.")
                return redirect("hayvanlar:index")
    if query:
        hayvanlar=Hayvan.objects.filter(Q(type__icontains=query) | Q(genus__icontains=query) | Q(name__icontains=query) )
        if hayvanlar: 
            context={"hayvanlar":hayvanlar,"form":form}
            return render(request,"animals.html",context)
        else:
            messages.warning(request,"Aradığınız Kriterlerde Kayıt Bulunamadı.")
            context={"hayvanlar":hayvanlar,"form":form}
            return render(request,"animals.html",context)
    context={"hayvanlar":hayvanlar,"form":form}
    return render(request,"animals.html",context)

@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def hayvan_delete(request,id):
    animals = get_object_or_404(Hayvan,id = id)
    animals.delete()
    messages.success(request,"Kayıt Başarıyla Silindi")

    return redirect("hayvanlar:animals")

@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def hayvan_update(request,id):
    hayvanlar=Hayvan.objects.all()
    instance = get_object_or_404(Hayvan,id = id)
    form = HayvanForm(request.POST or None,instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Kayıt başarıyla güncellendi")
        return redirect(request.META.get('HTTP_REFERER'))

    context={"hayvanlar":hayvanlar,"form":form}
    return render(request,"edit_animals.html",context)

@login_required(login_url = "user:sign_in")
def sahipler(request):

    sahipler=HayvanSahibi.objects.all()
    # hayvan = sahipler.hayvan_set.all()
    form2=SahipForm()

    query=request.GET.get('search')
    if request.method == 'POST':
        form = SahipForm(request.POST)
        try:
            if form.is_valid:
                hayvan_sahibi = form.save(commit=False)
                hayvan_sahibi.save()
                messages.success(request,"Hayvan Sahibi Başarılı Bir Şekilde Eklendi")
                return redirect("hayvanlar:hayvanSahipleri")
        except(ValueError):
            messages.warning(request,"Lütfen Formu Uygun Bir Şekilde Doldurun.")
            return redirect("hayvanlar:index")

    if query:
        sahipler=HayvanSahibi.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
        if sahipler:
            context={"sahipler":sahipler,"form2":form2}
            return render(request,"hayvanSahipleri.html",context)
        else:
            messages.warning(request,"Aradığınız Kriterlerde Kayıt Bulunamadı.")
            context={"sahipler":sahipler,"form2":form2}
            return render(request,"hayvanSahipleri.html",context)
    context={"sahipler":sahipler,"form2":form2}
    return render(request,"hayvanSahipleri.html",context)

@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def sahipler_update(request,id):
     
    sahipler=HayvanSahibi.objects.all()
    instance = get_object_or_404(HayvanSahibi,id = id)
    form = SahipForm(request.POST or None,instance = instance)
    try:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,"Kayıt başarıyla güncellendi")
            return redirect(request.META.get('HTTP_REFERER'))
    except(ValueError):
                messages.warning(request,"Lütfen Formu Uygun Bir Şekilde Doldurun.") 
                return render(request,"edit_owner.html",context)
    context={"sahipler":sahipler,"form":form}
    return render(request,"edit_owner.html",context)


@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def sahipler_delete(request,id):
    owner = get_object_or_404(HayvanSahibi,id = id)
    owner.delete()
    messages.success(request,"Kayıt Başarıyla Silindi")
    return redirect("hayvanlar:hayvanSahipleri")

@login_required(login_url = "user:sign_in")
def sahip_detay(request,id):
    form = get_object_or_404(HayvanSahibi,id = id)
    hayvan = form.hayvan_set.all()
    context={"form":form,"hayvan":hayvan}
    return render(request,"sahip_detay.html",context)

@login_required(login_url = "user:sign_in")
def hayvan_detay(request,id):
    form = get_object_or_404(Hayvan,id = id)
    context={"form":form}
    return render(request,"hayvan_detay.html",context)

@login_required(login_url = "user:sign_in")
def alertmessage(request):
	messages.warning(request,'Bu İşlemi Yapmaya Yetkiniz Yok')
	return redirect("hayvanlar:animals")
