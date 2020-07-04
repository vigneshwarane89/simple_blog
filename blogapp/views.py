from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import BlogArticle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
"""
typed in shell

u=(User.objects.all())
testuser=u[0]
simple=BlogArticle()
simple.title="Sample"
simple.blog_content="This is a sample blog"
simple.author=testuser

"""





def index(request):
	#return HttpResponse("HI!!!")
	blogs=BlogArticle.objects.all()
	usname=""
	pwd=""
	if request.method=='POST':
		usname=request.POST['username']
		pwd=request.POST['password']

	user=authenticate(username=usname,password=pwd)
	if user is not None:
		login(request,user)
		return(render(request,'base.html',{"blogs":blogs},{"user":user}))
	return(render(request,'base.html',{"blogs":blogs},{"user":None}))

def createblog(request):
	new=BlogArticle()
	new.title= request.POST['title']
	new.author= request.user
	new.blog_content=request.POST['blog_content']
	return(render(request,'base.html',{"blogs":blogs},{"user":user}))
