from math import ceil
from django.shortcuts import render,HttpResponse
from app.models import *
from django.contrib import messages
# Create your views here.
def portfolio(request):
    allProds=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"app/portfolio.html", params)

def contact1(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        emailID=request.POST.get('email')
        desc=request.POST.get('desc')
        phone=request.POST.get('pnumber')

        myquery=contact(name=name, emailID=emailID, desc=desc, phone=phone )
        myquery.save()
        messages.info(request, "We will get back to you soon.....")
    return render(request, 'app/contact.html')


def checkout(request):
    return render(request, 'app/checkout.html')

def services(request):
    return render(request, 'app/services.html')

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')