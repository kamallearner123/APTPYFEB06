from django.shortcuts import render
from news import newstoday
import os
from django.http import HttpResponse
from .forms import NewsSearchForm
from django.shortcuts import render, redirect
from .forms import CarServiceForm, CarEstimateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def print_request_info(request):
    # Print in color for debugging
    print("\033[92m" + "Request method: " + request.method + "\033[0m")  # Green text
    print("\033[93m" + "Request path: " + request.path + "\033[0m")  # Yellow text
    print("\033[94m" + "Request body: " + str(request.body) + "\033[0m")  # Blue text
    print("\033[95m" + "Request headers: " + str(request.headers) + "\033[0m")  # Purple text
    print("\033[96m" + "Request GET: " + str(request.GET) + "\033[0m")  # Cyan text
    print("\033[97m" + "Request POST: " + str(request.POST) + "\033[0m")  # White text
    print("\033[91m" + "Request user: " + str(request.user) + "\033[0m")  # Red text
    print("\033[92m" + "Request session: " + str(request.session) + "\033[0m")  # Green text

def news_today(request):
    print_request_info(request)  # Call the function to print request info
    newstoday.get_todays_news()
    CWD = os.path.dirname(os.path.realpath(__file__))
    NEWS_HTML_FILE = CWD+"/data/newstoday.html"
    try:
        with open(NEWS_HTML_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "No news available"
    return HttpResponse(content)

@login_required
def search_news(request):

    if request.method == "POST":
        print("***** in POST*****")
        keyword = request.POST.get("keyword")
        # get user from request
        user = request.user
        # Save the search to the database
        # Assuming you have a model named NewsSearch

        return HttpResponse(f"You searched for: {keyword}")
    else :
        print("***** in GET *****")
        form = NewsSearchForm()
        # print request GET details
        print("\033[92m" + "Request GET: " + str(request.GET) + "\033[0m")
        print("\033[93m" + "Request POST: " + str(request.POST) + "\033[0m")
        print("\033[94m" + "Request user: " + str(request.user) + "\033[0m")
        print("\033[95m" + "Request session: " + str(request.session) + "\033[0m")

        
        return render(request, "search_form.html", {'form': form})
    
@login_required
def create_car_service(request):
    if request.method == 'POST':
        form = CarServiceForm(request.POST)
        #print form with all the data with color
        print("\033[92m" + "Form data: " + str(form.data) + "\033[0m")

        if form.is_valid():
            car_service = form.save(commit=False)
            #car_service.user = request.user  # Set logged-in user
            car_service.save()
            return render(request, 'service/service_success.html', {'service': car_service})
    else:
        form = CarServiceForm()

    return render(request, 'service/car_service_form.html', {'form': form})

@login_required
def service_success(request):
    return render(request, 'service/service_success.html')

@login_required
def car_service(request):
    return render(request, 'service/car_service.html')

@login_required
def create_car_estimate(request):
    if request.method == 'POST':
        form = CarEstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.created_by = request.user
            estimate.save()
            return redirect('estimate_success')  # Create a success page/view
    else:
        form = CarEstimateForm()
    return render(request, 'service/car_service_form.html', {'form': form})

def estimate_success(request):
    return render(request, 'service/estimate_success.html')