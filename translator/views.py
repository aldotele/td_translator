from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
import json


def home(request, slug = "it"):
    context = {}
    context["slug"] = slug
    return render(request, 'home.html', context)


def translate(request):
    #print(request)
    tr = Translator()
    context = {}
    data = json.loads(request.body)
    word = data['tr_content']
    dest_language = data['slug']
    out = tr.translate(word, dest=dest_language).text
    context['translated'] = out
    context['slug'] = dest_language
    #print(context)
    return HttpResponse(json.dumps(context), content_type="application/json")


if __name__ == '__main__':
    test = Translator()
    output = test.translate("word", dest="it")
    print(output.extra_data['possible-translations'])