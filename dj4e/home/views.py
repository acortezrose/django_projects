from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
	response = """<html><head><meta name="wa4e" content="65b9eea6e1cc6bb9f0cd2a47751a186f"></head>
<body><p>Hello World</p></body></html> """
	return HttpResponse(response)
