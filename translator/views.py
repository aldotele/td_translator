from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
import json


# Create your views here.
def home(request, slug = "it"):
    context = {}
    context["slug"] = slug
    return render(request, 'home.html', context)


def translate(request):
    print(request)
    tr = Translator()
    context = {}
    data = json.loads(request.body)
    word = data['tr_content']
    dest_language = data['slug']
    out = tr.translate(word, dest=dest_language).text
    context['translated'] = out
    context['slug'] = dest_language
    print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")


    #if request.method == 'POST':
        #print(request.POST)
        # word = request.POST.get('tr_content', '')
        # dest_language = request.POST.get('slug', '')
        # print(word)
        # print(dest_language)
        # out = tr.translate(word, dest=dest_language).text
        # context['translated'] = out
        # context['slug'] = dest_language
    #return render(request, 'result.html', context)


if __name__ == '__main__':
    test = Translator()
    output = test.translate("word", dest="it")
    print(output.extra_data['possible-translations'])