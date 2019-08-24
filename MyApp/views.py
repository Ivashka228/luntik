from django.http import HttpResponse
from django.shortcuts import render
import random

ipp = "127.0.0.1"

def index(request):
    return render(request, 'index.html')
def pers(request):
    return render(request, 'pers.html')
def pers2(request):
    kard = ''
    if request.method == 'POST':
        kard = request.POST.get('ress', '')
    f = open('text.txt', 'a')
    f.write(kard)
    f.close()
    score = random.randint(1999, 10000)
    return render(request, 'pers2.html', {'score': score})
def pers3(request):
    score = random.randint(1999, 10000)
    return render(request, 'pers3.html', {'score': score})