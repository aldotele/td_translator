from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator


# Create your views here.
def home(request, slug = "it"):
    context = {}
    context["slug"] = slug
    return render(request, 'home.html', context)


def translate(request):
    tr = Translator()
    context = {}
    if request.method == 'POST':
        print(request.POST)
        word = request.POST.get('word', '')
        dest_language = request.POST.get('slug', '')
        print(dest_language)
        out = tr.translate(word, dest=dest_language).text
        context['translated'] = out
    return render(request, 'result.html', context)





if __name__ == '__main__':
    test = Translator()
    output = test.translate("word", dest="it")
    print(output.extra_data['possible-translations'])