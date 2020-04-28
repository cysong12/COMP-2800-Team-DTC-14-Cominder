from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Home page successfully rendered!!!!! WOOOOOOOOOOO</h1>')

def about(request):
	return HttpResponse('<h1>Does the About page render as well???? YESSSSSSSSSSSSSS</h1>')