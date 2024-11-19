from django.shortcuts import render
from .models import Order
from .forms import  ContactForm

# Create your views here.


def cart(request):
     all_blogs = Order.objects.all().order_by('-created')


     if request.POST.get('fullname'):
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('massage'))

     context = {
        'number': 100,
        'string': 'Hello My World',
        'text': '<i>This is a text </i>',
        'newText': 'Random info',
        'all_blogs': all_blogs,
        'form': ContactForm (request.POST or None),

    }
     return render(request , 'cart.html' , context=context)

def checkout(request,pk):
    order_post = Order.objects.get(pk=pk)
    context = {
        'order_post' : order_post
    }
    
    return render(request , 'checkout.html',context=context)

def wishlist(request, pk):
    order_post = Order.objects.grt(pk==pk)
    context = {
        'order_post ' : order_post
    }
    return render(request ,  "wishlist.html" , context= context)
