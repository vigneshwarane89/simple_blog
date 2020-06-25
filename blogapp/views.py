from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse("HI!!!")
	return render(request,'base.html',{'testvar':'h1!NEW'})