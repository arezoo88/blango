from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

def index(request):
  return render(request, "blog/index.html")
