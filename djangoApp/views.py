from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from .models import Employee

# Create your views here.

class HomeView(View):
    def get(self, request):
        emp = Employee.objects.all()
        return render(request, 'home.html',{'employee':emp})

    def post(self, request):
        ename = request.POST.get('ename')
        edesg  = request.POST.get('edesg')
        esal = request.POST.get('esal')
        e = Employee(ename=ename, edesg=edesg, esal=esal)
        e.save()
        emp = Employee.objects.all()
        return render(request, 'home.html',{'employee':emp})


class DelteView(View):
    def get(self, request,id):
        e = Employee.objects.get(id=id)
        e.delete()
        return HttpResponseRedirect('/')
    

class UpdateView(View):
    def post(self, request, id):
        emp = Employee.objects.get(id=id)
        ename = request.POST.get('ename')
        edesg  = request.POST.get('edesg')
        esal = request.POST.get('esal')
        e = Employee(id=id,ename=ename, edesg=edesg, esal=esal)
        e.save()
        return render(request, 'update.html',{'emp':emp})

    def get(self, request, id):
        emp = Employee.objects.get(id=id)
        return render(request, 'update.html',{'emp':emp})



