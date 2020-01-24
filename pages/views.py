from django.shortcuts import render
from accounts.forms import ContactUsForm 
# Create your views here.
def about_me(request):
    """
    A View that renders the about me page
    """
    return render(request, "about.html")
    
def faq_page(request):
    return render(request, "faq.html")

def contact(request):
    form = ContactUsForm()
    return render(request, "contact.html", {'form': form})