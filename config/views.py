from django.http import HttpResponse

def index(reauest):
    return HttpResponse('Hello. This is main page!')