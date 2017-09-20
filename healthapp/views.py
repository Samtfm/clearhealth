from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import urllib
# Create your views here.
def index(request):
    return HttpResponse("Heya, you've made it to the Health App Index!")

def auth(request):
    # redirect_uri = "https://clear-health.herokuapp.com/"
    redirect_uri = 'http://localhost:8000/app/'
    client_id = "ykmll9feaxeRc6g04N8Ysv67z7UKAjrUQ1KwvU87"
    querystring = urllib.parse.urlencode({
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "client_id": client_id,
        # "scope": scopes
    });
    # response = HttpResponseRedirect(redirect_to=url)
    response = redirect("https://onpatient.com/o/authorize/?" + querystring)
    # response = redirect('https://onpatient.com/authorize')
    # Set 'Test' header and then delete
    response['redirect_uri'] = 'https://yahoo.com'
    return response
