from django.shortcuts import render
from django.http import HttpResponse
from .task import sleepy, send_email_task


# Create your views here.

def index(request):
    send_email_task.delay()
    return HttpResponse("<h1>Task of message done!</H1>")
