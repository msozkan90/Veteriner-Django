
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AnimalsForm,OwnersForm
from hayvanlar.models import AnimalOwners,Animals
from django.contrib import messages
from .models import *
# from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    return render(request,"index.html")

@login_required(login_url = "user:sign_in")
def animals(request):
    # query=request.GET.get('search')
    hayvanlar=Animals.objects.all()
    paginator = Paginator(hayvanlar, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form=AnimalsForm()
    if request.method == 'POST':
        form = AnimalsForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                messages.success(request,"You added animal successfully")
                return redirect("hayvanlar:animals")
        except(ValueError):
                messages.warning(request,"Please fill the form correctly")
                return redirect("hayvanlar:animals")
    # From here used Data Tables
    # if query:
    #     hayvanlar=Hayvan.objects.filter(Q(type__icontains=query) | Q(genus__icontains=query) | Q(name__icontains=query) )
    #     if hayvanlar: 
    #         context={"hayvanlar":hayvanlar,"form":form,"page_obj":page_obj}
    #         return render(request,"animals.html",context)
    #     else:
    #         messages.warning(request,"Aradığınız Kriterlerde Kayıt Bulunamadı.")
    #         context={"hayvanlar":hayvanlar,"form":form,"page_obj":page_obj}
    #         return render(request,"animals.html",context)
    context={"hayvanlar":hayvanlar,"form":form,"page_obj":page_obj}
    return render(request,"animals.html",context)

@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def animal_delete(request,id):
    animals = get_object_or_404(Animals,id = id)
    animals.delete()
    messages.success(request,"Data deleted successfully")

    return redirect("hayvanlar:animals")

@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def animal_update(request,id):
    hayvanlar=Animals.objects.all()
    instance = get_object_or_404(Animals,id = id)
    form = AnimalsForm(request.POST or None,instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request,"Data updated successfully")
        return redirect(request.META.get('HTTP_REFERER'))

    context={"hayvanlar":hayvanlar,"form":form}
    return render(request,"edit_animals.html",context)

@login_required(login_url = "user:sign_in")
def owners(request):

    owners=AnimalOwners.objects.all()
    paginator = Paginator(owners, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form2=OwnersForm()

    # query=request.GET.get('search')
    if request.method == 'POST':
        form = OwnersForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                messages.success(request,"You added animal owner successfully")
                return redirect("hayvanlar:animalowners")
        except(ValueError):
            messages.warning(request,"Please fill the form correctly")
            return redirect("hayvanlar:index")

    # if query:
    #     sahipler=HayvanSahibi.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
    #     if sahipler:
    #         context={"sahipler":sahipler,"form2":form2,"page_obj":page_obj}
    #         return render(request,"hayvanSahipleri.html",context)
    #     else:
    #         messages.warning(request,"Aradığınız Kriterlerde Kayıt Bulunamadı.")
    #         context={"sahipler":sahipler,"form2":form2,"page_obj":page_obj}
    #         return render(request,"hayvanSahipleri.html",context)
    context={"owners":owners,"form2":form2,"page_obj":page_obj}
    return render(request,"animalowners.html",context)

@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def owner_update(request,id):
     
    sahipler=AnimalOwners.objects.all()
    instance = get_object_or_404(AnimalOwners,id = id)
    form = OwnersForm(request.POST or None,instance = instance)
    try:
        if form.is_valid():
            form.save()
            messages.success(request,"Data updated successfully")
            return redirect(request.META.get('HTTP_REFERER'))
    except(ValueError):
                messages.warning(request,"Please fill the form correctly") 
                return render(request,"edit_owner.html",context)
    context={"sahipler":sahipler,"form":form}
    return render(request,"edit_owner.html",context)


@user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
def owner_delete(request,id):
    owner = get_object_or_404(AnimalOwners,id = id)
    owner.delete()
    messages.success(request,"Data deleted successfully")
    return redirect("hayvanlar:animalowners")

@login_required(login_url = "user:sign_in")
def owner_detail(request,id):
    form = get_object_or_404(AnimalOwners,id = id)
    hayvan = form.animals_set.all()
    context={"form":form,"hayvan":hayvan}
    return render(request,"owner_detail.html",context)

@login_required(login_url = "user:sign_in")
def animal_detail(request,id):
    form = get_object_or_404(Animals,id = id)
    context={"form":form}
    return render(request,"animal_detail.html",context)

@login_required(login_url = "user:sign_in")
def alertmessage(request):
	messages.warning(request,'You have no permission to do this')
	return redirect("hayvanlar:index")
