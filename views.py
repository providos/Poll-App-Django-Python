from django.http import HttpResponse 
# in django we use modules, these modules are built in scripts to help us automate certain tasks
# in this case we use the "import" statement to import the submodule .http from the django library?
# from the .http module we use theHttpResponse script

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
