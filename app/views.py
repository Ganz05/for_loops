from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'Ganesh'}
    return render(request,'forloop.html',context=d)
