from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, This is my first web app.</h1>")