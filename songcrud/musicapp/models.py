from django.db import models
from django.http import httpresponse
# Create your models here.
def index(request):
  return httpresponse("Yayyyy")