
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AnimalsForm,OwnersForm
from hayvanlar.models import AnimalOwners,Animals
from django.contrib import messages
from .models import *
from .mixins import EditLoginRequiredMixin,AdminLoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import reverse
# from django.urls import reverse_lazy
# from django.db.models import Q
# from django.core.paginator import Paginator


class IndexPageView(generic.TemplateView):
    template_name = "index.html"

class AnimalCreateView(EditLoginRequiredMixin,generic.CreateView,generic.ListView):
    template_name = "animals.html"
    form_class = AnimalsForm
    context_object_name = "hayvanlar"
    def get_success_url(self):
        return reverse("hayvanlar:animals")
    def get_queryset(self):
        hayvanlar=Animals.objects.all()
        return hayvanlar
    def form_valid(self, form):
        form = AnimalsForm(self.request.POST)
        try:
            if form.is_valid:
                forms = form.save(commit=False)
                forms.save()
                messages.success(self.request,"You added animal successfully")
                return super(AnimalCreateView, self).form_valid(form)
        except(ValueError):
                messages.warning(self.request,"Please fill the form correctly")
                return super(AnimalCreateView, self)

class AnimalUpdateView(AdminLoginRequiredMixin,generic.UpdateView,generic.ListView):
    template_name = "edit_animals.html"
    form_class = AnimalsForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hayvanlar'] = Animals.objects.all()
        return context
    def get_success_url(self):
        return reverse("hayvanlar:animals")
    def get_queryset(self):
        animal=Animals.objects.filter(id=self.kwargs['pk'])
        return animal 
    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this animal")
        return super(AnimalUpdateView, self).form_valid(form)

class AnimalDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "animal_delete.html"
    def get_success_url(self):
        messages.info(self.request, "You have successfully deleted")
        return reverse("hayvanlar:animals")
    def get_queryset(self):
        animal=Animals.objects.filter(id=self.kwargs['pk'])
        return animal 

class AnimalDetailView(AdminLoginRequiredMixin,generic.DetailView):
    template_name = "animal_detail.html"
    context_object_name = "form"
    def get_queryset(self):
        animal=Animals.objects.filter(id=self.kwargs['pk'])
        return animal 

class OwnerCreateView(EditLoginRequiredMixin,generic.CreateView,generic.ListView):
    template_name = "animalowners.html"
    form_class = OwnersForm
    context_object_name = "owners"
    def get_success_url(self):
        return reverse("hayvanlar:animalowners")
    def get_queryset(self):
        owners=AnimalOwners.objects.all()
        return owners
    def form_valid(self, form):
        form = OwnersForm(self.request.POST)
        if form.is_valid:
            forms = form.save(commit=False)
            forms.save()
            messages.success(self.request,"You added owner successfully")
            return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(AdminLoginRequiredMixin,generic.UpdateView,generic.ListView):
    template_name = "edit_owner.html"
    form_class = OwnersForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owners'] = AnimalOwners.objects.all()
        return context
    def get_success_url(self):
        return reverse("hayvanlar:animalowners")
    def get_queryset(self):
        animal=AnimalOwners.objects.filter(id=self.kwargs['pk'])
        return animal 
    def form_valid(self, form):
        form.save()
        messages.info(self.request, "You have successfully updated this owner")
        return super(OwnerUpdateView, self).form_valid(form)

class OwnerDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "owner_delete.html"
    def get_success_url(self):
        messages.info(self.request, "You have successfully deleted")
        return reverse("hayvanlar:animalowners")
    def get_queryset(self):
        owner=AnimalOwners.objects.filter(id=self.kwargs['pk'])
        return owner 

class OwnerDetailView(AdminLoginRequiredMixin,generic.DetailView):
    template_name = "owner_detail.html"
    context_object_name = "form"
    def get_queryset(self):
        animal=AnimalOwners.objects.filter(id=self.kwargs['pk'])
        return animal 

# def index(request):
#     return render(request,"index.html")


# @login_required(login_url = "user:sign_in")
# def animals(request):
#     # query=request.GET.get('search')
#     hayvanlar=Animals.objects.all()
#     # paginator = Paginator(hayvanlar, 10)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)
#     form=AnimalsForm()
#     if request.method == 'POST':
#         form = AnimalsForm(request.POST)
#         try:
#             if form.is_valid:
#                 form.save()
#                 messages.success(request,"You added animal successfully")
#                 return redirect("hayvanlar:animals")
#         except(ValueError):
#                 messages.warning(request,"Please fill the form correctly")
#                 return redirect("hayvanlar:animals")
#     # From here used Data Tables
#     # if query:
#     #     hayvanlar=Hayvan.objects.filter(Q(type__icontains=query) | Q(genus__icontains=query) | Q(name__icontains=query) )
#     #     if hayvanlar: 
#     #         context={"hayvanlar":hayvanlar,"form":form,"page_obj":page_obj}
#     #         return render(request,"animals.html",context)
#     #     else:
#     #         messages.warning(request,"Aradığınız Kriterlerde Kayıt Bulunamadı.")
#     #         context={"hayvanlar":hayvanlar,"form":form,"page_obj":page_obj}
#     #         return render(request,"animals.html",context)
#     context={"hayvanlar":hayvanlar,"form":form}
#     return render(request,"animals.html",context)



# @user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
# def animal_update(request,id):
#     hayvanlar=Animals.objects.all()
#     instance = get_object_or_404(Animals,id = id)
#     form = AnimalsForm(request.POST or None,instance = instance)
#     try:
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Data updated successfully")
#             return redirect(request.META.get('HTTP_REFERER'))
#     except(ValueError):
#         messages.warning(request,"Please fill the form correctly") 
#         return render(request,"edit_animals.html",context)

#     context={"hayvanlar":hayvanlar,"form":form}
#     return render(request,"edit_animals.html",context)


# @user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
# def animal_delete(request,id):
#     animals = get_object_or_404(Animals,id = id)
#     animals.delete()
#     messages.success(request,"Data deleted successfully")

#     return redirect("hayvanlar:animals")

# @login_required(login_url = "user:sign_in")
# def animal_detail(request,id):
#     form = get_object_or_404(Animals,id = id)
#     context={"form":form}
#     return render(request,"animal_detail.html",context)

# @login_required(login_url = "user:sign_in")
# def owners(request):

#     owners=AnimalOwners.objects.all()
#     # paginator = Paginator(owners, 10)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)
#     form=OwnersForm()
#     if request.method == 'POST':
#         form = OwnersForm(request.POST)
#         try:
#             if form.is_valid:
#                 form.save()
#                 messages.success(request,"You added animal owner successfully")
#                 return redirect("hayvanlar:animalowners")
#         except(ValueError):
#             messages.warning(request,"Please fill the form correctly")
#             return redirect("hayvanlar:index")
#     context={"owners":owners,"form":form}
#     return render(request,"animalowners.html",context)

# @user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
# def owner_update(request,id):
     
#     owners=AnimalOwners.objects.all()
#     instance = get_object_or_404(AnimalOwners,id = id)
#     form = OwnersForm(request.POST or None,instance = instance)
#     try:
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Data updated successfully")
#             return redirect(request.META.get('HTTP_REFERER'))
#     except(ValueError):
#                 messages.warning(request,"Please fill the form correctly") 
#                 return render(request,"edit_owner.html",context)
#     context={"owners":owners,"form":form}
#     return render(request,"edit_owner.html",context)


# @user_passes_test(lambda u: u.is_superuser,login_url = "hayvanlar:alertmessage")
# def owner_delete(request,id):
#     owner = get_object_or_404(AnimalOwners,id = id)
#     owner.delete()
#     messages.success(request,"Data deleted successfully")
#     return redirect("hayvanlar:animalowners")

# @login_required(login_url = "user:sign_in")
# def owner_detail(request,id):
#     form = get_object_or_404(AnimalOwners,id = id)
#     hayvan = form.animals_set.all()
#     context={"form":form,"hayvan":hayvan}
#     return render(request,"owner_detail.html",context)



@login_required(login_url = "user:sign_in")
def alertmessage(request):
	messages.warning(request,'You have no permission to do this')
	return redirect("hayvanlar:index")
