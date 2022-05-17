from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from article.models import Article

# bunun amacı articleları .all() listelemek ve her
# birine link verip edit sayfasına yönlendirmek
def article_index(request):
    articles = Article.objects.all()
    if articles:
        return render(request, 'list_article.html', {
            'articles': articles
        })
    else:
        return HttpResponse('<b>hoşgeldin, kayıt eklemek için tıkla </b>')

# bunun tek amacı yeni article olustur formunu render etmek
def article_new_form(request):
    return render(request, 'new_article.html')
 
# bu POST ile bu methoda taşınan veriyi
# DB'ye kaydedip listeleme sayfasına döndürecek
def article_create(request):
    created_article = Article.objects.create(title=request.POST['title'], content=request.POST['content'])
    return redirect('/article/index')

# bunun amacı /article/bilmemne şeklinde gelen id'yi alıp
# DB'den çekip, formu render ederken içine vermek.
def article_edit(request, id):
    # tamam article ı buluyosun
    article = get_object_or_404(Article, id=id)
    
    context = {
        'article': article
    }
    return render(request, 'edit_article.html', context)


# bu methodun amacı edit formundan gelen veriyi (idyi de biliyoruz ya)
# DB'de o article ı güncelleyiop listeleme ekranına döndürmek
def article_update(request, id):
    # birden fazla kaydetme yolu varmıs

    # bu 1.
    # obj = Article.objects.get(id=id)
    # obj.title = request.POST['title']
    # obj.content = request.POST['content']
    # obj.save()

    # bu 2.
    updated_article = (Article.objects
        .filter(id=id)
        .update(title=request.POST['title'], content=request.POST['content'])
    )
    return redirect('/article/index')
   

def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/article/index')
