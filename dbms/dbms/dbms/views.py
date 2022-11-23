from django.shortcuts import render
from dbsqlite.models import dbsqlite
from . import views


def home(request):

    return render(request,'home.html')


def contact(request):
   d=''
   if request.method == 'POST':
     name        = request.POST.get('name')
     age         = request.POST.get('age')
     password    = request.POST.get('password')
     email       = request.POST.get('email')
     father_name = request.POST.get('father_name')
     our_image   = request.FILES.get('our_image')                 
     data=dbsqlite(name=name,age=age,password=password,email=email,father_name=father_name,our_image=our_image)
     d='sir check'
     data.save()
   return render(request,'contact.html',{
                      # 'd':d,
                      # 'name':name,
                      # 'age':age,
                      # 'password':password,
                      # 'email':email,
                      # 'father_name':father_name,
                      # 'our_image':our_image,
   })
                  
                  
def index(request):
    return render(request,'index.html')
  