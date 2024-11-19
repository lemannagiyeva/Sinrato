from django.shortcuts import render
from .models import Core
from .forms import  ContactForm


# Create your views here.




def time(request):

    all_blogs = Core.objects.all().order_by('-created')


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
    return render (request ,  'time.html' , context=context)

# def blog_detail(request , pk):
#     blog_post = Blogs.objects.get(pk=pk)
#     context = {
#         'blog_post' : blog_post
#     }
#     return render (request ,'blog-details.html' , context = context )

def about(request , pk):
    core_post = Core.objects.get(pk==pk)
    context = {
        'core_post' : core_post
    }
    return render(request , 'about.html' , context=context)



def index(request ,pk):
   core_post = Core.objects.get(pk==pk)
   context = {
      'core_post' : core_post
   }
       
   return render(request , 'index.html' ,context= context)

def contact_us(request,pk):
    core_post = Core.objects.get(pk==pk)
    context = {
      'core_post' : core_post
   }
    return render(request , 'contact-us.html',context= context)


def my_account(request,pk):
    core_post = Core.objects.get(pk==pk)
    context = {
      'core_post' : core_post
   }
    return render(request , 'my-account.html',context=context)




