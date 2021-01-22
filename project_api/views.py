from django.shortcuts import render

# Create your views here.
def project_api(request):
    return render(request, 'project_api.html')

def predict_changes(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))
