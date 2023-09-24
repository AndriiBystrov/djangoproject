from django.shortcuts import render

# Create your views here.
def index3(request):
    return render(request, "Main/index.html") 