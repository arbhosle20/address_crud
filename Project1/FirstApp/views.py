from django.shortcuts import render,redirect
from .forms import AddressModelForm
from .models import Address
from django .views import View



class addaddressview(View):
    def get(self,request):
        form = AddressModelForm()
        template_name = 'FirstApp/addaddress.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = AddressModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_address')
        template_name = 'FirstApp/addaddress.html'
        context = {'form':form}
        return render(request,template_name,context)

class showaddressview(View):
    def get(self,request):
        address_list = Address.objects.all()
        template_name = 'FirstApp/showaddress.html'
        context = {'address_list':address_list}
        return render(request,template_name,context)

class updateaddressview(View):
    def get(self,request,i):
        address = Address.objects.get(id=i)
        form = AddressModelForm(instance=address)
        template_name = 'FirstApp/addaddress.html'
        context ={'form':form}
        return render(request,template_name,context)
    def post(self ,request,i):
        address = Address.objects.get(id=i)
        form = AddressModelForm(request.POST,instance=address)
        if form.is_valid():
            form.save()
            return redirect('show_address')
        template_name = 'FirstApp/addaddress.html'
        context = {'form':form}
        return render(request,template_name,context)

class deleteaddressview(View):
    def get(self,request,i):
        address = Address.objects.get(id=i)
        template_name = 'FirstApp/deleteaddress.html'
        context = {'address':address}
        return render(request,template_name,context)

    def post(self,request,i):
        address = Address.objects.get(id=i)
        address.delete()
        return redirect('show_address')
