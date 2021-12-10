from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import profile
from django.http import HttpResponse

# Create your views here.
class HomePageView(ListView):
    model = profile
    template_name = 'home.html'
    queryset = profile.objects.all()
    context_object_name = 'all_posts_list' # new
  

def changePageView(request):
    return render(request, 'changepassword.html')

def regPageView(request):
    return render(request, 'register.html')

def loginPageView(request):
    return render(request, 'login.html')

def profilePageView(request):
    queryset = profile.objects.get(firstname="Manasaporn")
    return render(request, 'profile.html',{'all_posts_list':queryset})

def vocablistPageView(request):
    return render(request, 'vocab_list.html')

def vocabdelPageView(request):
    return render(request, 'vocab_del.html')

def contactPageView(request):
    return render(request, 'contact_us.html')

def aboutPageView(request):
    return render(request, 'about_us.html')

def editusrPageView(request):
    if request.method == 'POST':
        search = request.POST.get('nickname')
        profile.objects.filter(firstname="Manasaporn").update(nickname=search)
        queryset = profile.objects.get(firstname="Manasaporn")
        return render(request, 'profile.html',{'all_posts_list':queryset})
    else: 
        queryset = profile.objects.get(firstname="Manasaporn")
    return render(request, 'edit_user.html',{'all_posts_list':queryset})