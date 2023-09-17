from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
import random 


def home(request):

    random_number = random.randint(1,3)
    article_obj = Article.objects.get(id=random_number)

    my_list = [102, 13, 342, 1331, 213]
  
    article_queryset = Article.objects.all()
    context = {
        'obj_list':article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

   
    
    return render(request, 'home.html', context)
