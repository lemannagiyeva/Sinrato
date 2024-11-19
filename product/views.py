from django.shortcuts import render
from .models import Product
from .forms import  ContactForm

# Create your views here.


def product(request):
     all_product = Product.objects.all().order_by('-created')
     print(all_product)


     if request.POST.get('fullname'):
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('massage'))

     context = {
        'number': 100,
        'string': 'Hello My World',
        'text': '<i>This is a text </i>',
        'newText': 'Random info',
        'all_product': all_product,
        'form': ContactForm(request.POST or None),

    }
        

     return render(request ,'shop.html' ,context=context)

def shop(request, pk):
    product_post = Product.objects.get(pk=pk)
    context={
        'product_post' : product_post
    }
    return render(request , 'product.html',context=context)

