from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("Heya, you've made it to the Health App Index!")

def auth(request):
    response = redirect('https://onpatient.com/authorize')
    # Set 'Test' header and then delete
    response['redirect_uri'] = 'https://yahoo.com'
    return response
