from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
	# Get all the jobs and send them back to the render
	jobs = Job.objects
	return render(request, 'jobs/home.html', {'jobs':jobs})