from django.shortcuts import render

# Create your views here.
def project_api(request):
    return render(request, 'project_api.html')
