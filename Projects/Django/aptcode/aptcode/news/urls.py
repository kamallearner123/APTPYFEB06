from django.urls import path
from news import views as news_views
urlpatterns = [
    #path('', news_views.news_today),  # Added newly
    path('', news_views.news_today),
    path('search/', news_views.search_news, name='search_news'),  # Added newly    
    path('service/', news_views.create_car_service, name='create_car_service'),
    path('estimate/', news_views.create_car_estimate, name='create_estimate'),
    path('estimate/success/', news_views.estimate_success, name='estimate_success'),
]