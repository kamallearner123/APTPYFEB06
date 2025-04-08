from django.db import models
from django.contrib.auth.models import User

class NewsSearch(models.Model):
    keyword = models.CharField(max_length=100)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.keyword} @ {self.search_time.strftime('%Y-%m-%d %H:%M:%S')}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.TextField(blank=True)  # Or any other fields you need

    def __str__(self):
        return self.user.username

# Create new model to make entries for a car service
class CarService(models.Model):
    service_date = models.DateTimeField(auto_now_add=True)
    car_model = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    service_notes = models.TextField(blank=True)
    service_completed = models.BooleanField(default=False)
    service_completed_date = models.DateTimeField(null=True, blank=True)
    service_completed_notes = models.TextField(blank=True)
    service_completed_by = models.ForeignKey(User, null=True, blank=True, related_name='completed_services', on_delete=models.SET_NULL)
    service_completed_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    service_completed_notes = models.TextField(blank=True)

    
    def __str__(self):
        return f"{self.car_model} - {self.service_type} on {self.service_date.strftime('%Y-%m-%d %H:%M:%S')}"

class CarEstimate(models.Model):
    name = models.CharField(max_length=100)
    trn_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    emirate = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=20)
    estimate_number = models.CharField(max_length=100)
    date = models.DateField()
    ref_number = models.CharField(max_length=100, blank=True, null=True)
    est_days = models.IntegerField(default=0)
    payment_terms = models.TextField(blank=True)
    registration = models.CharField(max_length=100)
    make_model = models.CharField(max_length=100)
    year = models.IntegerField()
    chassis_no = models.CharField(max_length=100)
    km_miles = models.CharField(max_length=50)

    remarks = models.TextField(blank=True, null=True)
    net_total = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    total_incl_vat = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Estimate {self.estimate_number} for {self.name}"    