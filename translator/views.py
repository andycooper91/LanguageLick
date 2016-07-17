from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
import os
import codecs
from .models import *
import datetime

def index(request):
    art = Article.objects.all().order_by('-id')[:15]
    articles = []
    for a in art:
        articles.append((a.headline,a.pk))
    context = {'articles':articles}
    return render(request,'translator/index.html',context)




def article(request, article_id):
    #template = loader.get_template('translator/index.html')
    #module_dir = os.path.dirname(__file__)
    #file_path = os.path.join(module_dir, '/texts/1.txt')
    #print module_dir
    art = Article.objects.all().exclude(pk=article_id).order_by('-id')[:14]
    articles = []
    for a in art:
        articles.append((a.headline,a.pk))
    
    ar = Article.objects.get(pk=article_id)    
    with codecs.open("translator/texts/"+ar.file_name,'r',"latin-1") as f:
        count = 0
        for l in f:
            if count == 0:
                title = l
            if count == 2:
                author = l
            if count == 4:
                date = l
            if count == 6:
                text = l
            count += 1
    context = {'title':title,
                'author':author,
                'date':date,
                'text':text,
                'articles':articles
               }
    return render(request, 'translator/article.html', context)

def vocab(request):
    translations = Translation.objects.all()
    translation_data = []
    count = 0
    for t in translations:
        if count >= 50:
            break
        translation_data.append((t.from_phrase.phrase,t.to_phrase.phrase))
        count += 1
        
    art = Article.objects.all().order_by('-id')[:15]
    articles = []
    for a in art:
        articles.append((a.headline,a.pk))
        
    context = {'translation_data':translation_data,
               'articles':articles}
    return render(request,'translator/vocab.html',context)

def insertDatabase(request):
    ft = request.GET.get('fromText')
    tt = request.GET.get('toText')
    english = Language.objects.filter(language_code="en")[0]
    spanish = Language.objects.filter(language_code="es")[0]
    webText = PhraseSource.objects.filter(source_name="WebText")[0]        
    translation = PhraseSource.objects.filter(source_name="Translation")[0]      
    
    from_phrase_present = Phrase.objects.filter(phrase=ft).filter(language=spanish).filter(source=webText)
    to_phrase_present = Phrase.objects.filter(phrase=tt).filter(language=english).filter(source=translation)
       
    
    if len(from_phrase_present)>0:
        from_phrase_1 = from_phrase_present[0]
    else:
        from_phrase_1 = Phrase(phrase=ft,language=spanish,source=webText)
        from_phrase_1.save()

    
    if len(to_phrase_present)>0:
        to_phrase_1 = to_phrase_present[0]
    else:
        to_phrase_1 = Phrase(phrase=tt,language=english,source=translation)
        to_phrase_1.save()
    
    final_translation_present = Translation.objects.filter(from_phrase=from_phrase_1).filter(to_phrase=to_phrase_1)

    if len(final_translation_present) == 0:    
        final_translation = Translation(from_phrase=from_phrase_1,to_phrase=to_phrase_1,translation_date=datetime.datetime.now())
        final_translation.save()
    return HttpResponse("OK")
    
if __name__ == "__main__":
    translations = Translation.objects.all()
    translation_data = []
    count = 0
    for t in translations:
        print t