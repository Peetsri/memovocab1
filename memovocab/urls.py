from django.urls import path
from .views import HomePageView,regPageView,loginPageView,profilePageView,vocablistPageView,vocabdelPageView,contactPageView,aboutPageView,changePageView,editusrPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', aboutPageView, name='about_us'),
    path('register/', regPageView, name='register'),
    path('accounts/login/', loginPageView, name='login'),
    path('profile/', profilePageView, name='profile'),
    path('vocab_list/', vocablistPageView, name='vocab_list'),
    path('vocab_del/', vocabdelPageView, name='vocab_del'),
    path('contact_us/', contactPageView, name='contact_us'),
    path('changepassword/', changePageView, name='changepassword'),
    path('edit_user/', editusrPageView, name='edit_user'),
 
]