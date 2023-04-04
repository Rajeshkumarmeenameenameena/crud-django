from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .form import employeeform
# Create your views here.
def home(request):
    form=employeeform()
    if request.method=='POST':
        form=employeeform(request.POST)
        form.save()
        form=employeeform()
    data=employee.objects.all()
    
    context={
        'form':form,
        'data':data
     
    }
    return render(request,'app/index.html',context)

def deletedata(request,id):
    a=employee.objects.get(pk=id)
    a.delete()
    return redirect('/')

def updatepage(request,id):
    if request.method=="POST":
        data=employee.objects.get(pk=id)
        form=employeeform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        data=employee.objects.get(pk=id)
        form=employeeform(instance=data)
    context={
        'form':form
    }
    return render(request,'app/update.html',context)
    
