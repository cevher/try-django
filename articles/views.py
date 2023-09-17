from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.

def article_search_view(request):
    
    article_obj = None
    try:
        query = int(request.GET["q"])
    except:
        query = None

    if query is not None:
        article_obj = Article.objects.get(id=query)
    
    context ={
            "object": article_obj
        }
    
    return render(request, "articles/search.html",context=context )

@login_required
def article_create_view(request, id=None):
    form = ArticleForm(request.POST or None)
    context = {
            "form": form
            }

    if form.is_valid():
        obj = form.save() 
        context['form'] = ArticleForm()
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_object = Article.objects.create(title=title, content=content)
        # context['object'] = obj  #article_object
        # context['created'] = True
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None

    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj
    }
    return render(request, "articles/detail.html", context=context)