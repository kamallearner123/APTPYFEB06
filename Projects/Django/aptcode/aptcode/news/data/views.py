from django.shortcuts import render
from .forms import NewsSearchForm
import requests

def news_today(request):
    form = NewsSearchForm()
    articles = []

    if request.method == 'POST':
        form = NewsSearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            # Example using NewsAPI (replace YOUR_API_KEY)
            url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey=YOUR_API_KEY'
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])

    return render(request, 'news.html', {'form': form, 'articles': articles})
