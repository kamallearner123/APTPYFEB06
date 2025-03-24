from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def questions(request):
    template = loader.get_template("basic_questions.html")
    return HttpResponse(template.render({}, request))