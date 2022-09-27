from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('/polls/', views.index, name='index'),
    # ex: /polls/5/
    path('/polls/5/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('/polls/5/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('/polls/5/vote/', views.vote, name='vote'),
]