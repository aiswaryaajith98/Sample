from django.shortcuts import render

# Create your views here.
def Eg_Page(request):
    return render(request,'Eg.html')

def Eg2_Page(request):
    return render(request,'Eg2.html')


