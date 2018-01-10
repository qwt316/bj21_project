from django.http import HttpResponse

def index(request):
    return HttpResponse('index视图')



def index(request):
    return HttpResponse('<h1>视图</h>1')
