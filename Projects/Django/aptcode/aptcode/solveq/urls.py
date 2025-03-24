from django.urls import path
from . import views

urlpatterns = [
    # If the URL is http://127.0.0.1/members/, then the view function members() will be called.
    path('', views.questions, name='questions'),
]