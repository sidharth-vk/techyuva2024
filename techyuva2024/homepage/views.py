from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'homepage\index.html')

# custom 404 view
def custom_404(request, exception):
    return render(request, 'homepage\index.html', status=404)