from django.contrib import admin
from django.urls import path, include
from books import views

app_name = 'books'
urlpatterns = [
    #/books/
    path('', views.BooksListView.as_view(), name='index'),
    # path('', views.index, name='index'),

    #/search/
    path('search/', views.BooksSearchView.as_view(), name='search'),

    #/details view/
    # path('<int:book_id>',views.detail, name='detail'),
    path('<int:pk>',views.BooksDetailView.as_view(), name='detail'),

    #/add/
    # path('add/', views.add_book, name='add'),
    path('add/',views.BooksCreateView.as_view(), name='add'),
    
    #edit/
    # path('update/<int:id>/', views.update_book, name='update'),
    path('update/<int:pk>/', views.BooksUpdateView.as_view(), name='update'),

    #/delete/
    # path('delete/<int:id>/', views.delete_book, name='delete'),
    path('delete/<int:pk>/', views.BooksDeleteView.as_view(), name='delete'),

    #classed based views
    

]   
