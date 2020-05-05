from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', PageCreateView.as_view(), name='newpage'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
