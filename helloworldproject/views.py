from django.http import HttpResponse

def helloworldfunction(request):
  returnobject = HttpResponse("<h1>Hello World</h1>")
  return returnobject