from django.shortcuts import render

# Create your views here.
def project_api(request):
    return render(request, 'project_api.html')

def predict_changes(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        g1 = int(request.POST.get('g1'))
        g2 = int(request.POST.get('g2'))
        age = int(request.POST.get('age'))
        medu = int(request.POST.get('medu'))
        fedu = int(request.POST.get('fedu'))
        tt = int(request.POST.get('tt'))
        st = int(request.POST.get('st'))
        fail = int(request.POST.get('fail'))
        ft = int(request.POST.get('ft'))
        hs = int(request.POST.get('hs'))
        abs = int(request.POST.get('abs'))
