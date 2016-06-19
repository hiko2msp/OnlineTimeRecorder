from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
#    with open('templates/test.html') as f:
#        html = f.read()
#    return HttpResponse(html)
    # template = loader.get_template('test.html')
    return render(request, 'test.html', {})
    # return HttpResponse(template.render({}, request))
    
def second_page(request):
    return HttpResponse('Hello World２')
    
def hello2(request):
    with open('templates/hello2.html') as f:
        html = f.read()
    return HttpResponse(html)

def third_page(request):
    return HttpResponse('Hello World３')
    
def hello3(request):
    with open('templates/hello3.html') as f:
        html = f.read()
    return HttpResponse(html)
    