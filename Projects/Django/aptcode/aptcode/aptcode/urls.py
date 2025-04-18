"""
URL configuration for aptcode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from aptcode import views # Added newly
from news import views as news_views # Added newly
from django.contrib.auth.views import LogoutView

# URL patterns for the project
urlpatterns = [
    path("admin/", admin.site.urls),
    # Handled locally within main project
    path('', views.index, name='index'), # Added newly
    path('news/', include("news.urls")), # Added newly
    # If path is questions/, then include the solveq.urls (anohter app)
    path("questions/", include("solveq.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
