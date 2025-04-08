from django.http import HttpResponse
import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

def index(request):
    return HttpResponse("Web page to be developed")

