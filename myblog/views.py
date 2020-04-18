from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {'author': 'Dehai Kong',
     'title': 'post 1',
     'content': 'first content',
     'date_posted': '17th April 2020'
     },
    {'author': 'victor kong',
     'title': 'post 2',
     'content': 'sencond content',
     'date_posted': '18th April 2020'
     },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'myblog/home.html', context)


def about(request):
    return render(request, 'myblog/about.html', {'title': 'About!'})
