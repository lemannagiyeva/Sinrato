from django.shortcuts import render
from .models import Blogs
from .forms import  ContactForm
# Create your views here.

def blog (request):
    all_blogs = Blogs.objects.all()
    print(all_blogs)


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
        'form': ContactForm(request.POST or None),

    }
        

    return render(request ,'blog.html' ,context=context)


def blog_detail(request , pk):
    blog_post = Blogs.objects.get(pk=pk)
    context = {
        'blog_post' : blog_post
    }
    return render (request ,'blog-details.html' , context = context )



