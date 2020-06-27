from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogArticle
from django.contrib.auth.models import User
# Create your views here.
"""u=(User.objects.all())
testuser=u[0]
simple=BlogArticle()
simple.title="Sample"
simple.blog_content="This is a sample blog"
simple.author=testuser

"""

blogs=BlogArticle.objects.all()


def index(request):
	#return HttpResponse("HI!!!")
	return(render(request,'main.html',{"blogs":blogs}))