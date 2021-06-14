from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator


# Create your views here.
def home(request):
    return render(request, 'home.html')


def translate(request):
    
    tr = Translator()

    context = {}
    if request.method == 'POST':
        word = request.POST.get('word', '')
        out = tr.translate(word, dest="it").text

        #print(word)
        context['translated'] = out
    return render(request, 'result.html', context)


    #if request.method == "POST":
    #    word = request.POST
    #    print(word)
    #    return render(request, 'result.html')
