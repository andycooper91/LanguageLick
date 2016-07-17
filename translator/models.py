from django.db import models


class Language(models.Model):
    language_name = models.CharField(max_length=50)
    language_code = models.CharField(max_length=5)
    
    def __str__(self):
        return self.language_name

class PhraseSource(models.Model):
    source_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.source_name
    
class Phrase(models.Model):
    phrase = models.CharField(max_length=200)
    language = models.ForeignKey(Language)
    source = models.ForeignKey(PhraseSource)
    
    def __str__(self):
        return self.phrase
    
class Translation(models.Model):
    from_phrase = models.ForeignKey(Phrase,related_name='from_phrase')
    to_phrase = models.ForeignKey(Phrase,related_name='to_phrase')
    translation_date = models.DateTimeField('date published')
        
class Article(models.Model):
    headline = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
    file_name = models.CharField(max_length=200,blank=True,null=True,default=None)
    article_source = models.CharField(max_length=200)
    good_file = models.BooleanField(default=True)