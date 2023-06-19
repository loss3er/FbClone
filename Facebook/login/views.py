from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from login.models import Index

def login(request):
    # print(request.POST.get('sF_Name', 'default'))
    # print(request.POST.get('sL_Name', 'default'))
    # print(request.POST.get('sM_Email', 'default'))
    # print(request.POST.get('sPass', 'default'))
    # print(request.POST.get('sDate', 'default'))
    # print(request.POST.get('sMonth', 'default'))
    # print(request.POST.get('sYear', 'default'))
    # print(request.POST.get('flexRadioDefault', 'default'))
    if request.method == "POST":
       sF_Name = request.POST.get('sF_Name', 'default')
       sL_Name = request.POST.get('sL_Name', 'default')
       sM_Email = request.POST.get('sM_Email', 'default')
       sPass = request.POST.get('sPass', 'default')
       date = request.POST.get('sDate', 'default')
       month = request.POST.get('sMonth', 'default')
       year = request.POST.get('sYear', 'default')
       gen = request.POST.get('flexRadioDefault', 'default')
       Index = Index(sF_Name = sF_Name, sL_Name = sL_Name, sM_Email = sM_Email, sPass=sPass, date = datetime.today())
       Index.save()
    return render(request, 'login/index.html')

def home(request):
    return render(request, 'login/home.html')