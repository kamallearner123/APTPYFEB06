from django.http import HttpResponse
import os
from aptcode import newstoday

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

def index(request):
    return HttpResponse("Web page to be developed")

def news_today(request):
    newstoday.get_todays_news()
    CWD = os.path.dirname(os.path.realpath(__file__))
    NEWS_HTML_FILE = CWD+"/data/newstoday.html"
    try:
        with open(NEWS_HTML_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "No news available"
    return HttpResponse(content)