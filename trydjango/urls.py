 
from . import views
from django.contrib import admin
from django.urls import path
from articles import views as article_view
from accounts import views as accounts_view

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/',article_view.article_search_view, name='search_view'),
    path('articles/create/',article_view.article_create_view, name='create_view'),
    path('articles/<int:id>/',article_view.article_detail_view, name='articles' ),
    path('admin/', admin.site.urls),
    path('login/', accounts_view.login_view),
    path('logout/', accounts_view.logout_view),
    path('register/', accounts_view.register_view),
]
