from django.shortcuts import render,HttpResponse, redirect
from .models import Books
from .forms import BookForm
#classed based views
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
# pagination
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404



# Create your views here.


class BooksListView(ListView):
    paginate_by = 3
    model = Books
    queryset = Books.objects.all()
    template_name = 'books/index.html'
    context_object_name = 'book_list'

# to search the book by book title
class BooksSearchView(ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query  = self.request.GET.get('q')
        return Books.objects.filter(book_title__icontains=query)
        

# def index(request):
#     book_list = Books.objects.all()
#     paginator= Paginator(book_list,3)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)

#     return render(request, 'books/index.html', {'book_list':page_obj})


# def detail(request, book_id):
#     book = Books.objects.get(pk=book_id)
#     return render(request,'books/detail.html', {'book':book})

class BooksDetailView(DetailView):
    model = Books
    template_name = 'books/detail.html'
    context_object_name = 'book'

    

# def add_book(request):
#     form = BookForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('books:index')

#     return render(request, 'books/book_form.html', {'form':form})

# class based view for add book
class BooksCreateView(CreateView):
    model = Books
    fields = ['book_title', 'book_author', 'book_desc', 'book_price', 'book_rating', 'book_image']
    template_name = "books/book_form.html"  

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



# def update_book(request, id):
#     book = Books.objects.get(id=id)
#     form = BookForm(request.POST or None, instance=book)

#     if form.is_valid():
#         form.save()
#         return redirect('books:index')

#     return render(request,'books/book_form.html', {'form':form,'book':book})

class BooksUpdateView(UpdateView):
    model = Books
    fields = ['book_title', 'book_author', 'book_desc', 'book_price', 'book_rating', 'book_image']
    template_name = 'books/book_form.html'



# def delete_book(request, id):
#         book = Books.objects.get(id=id)

#         if request.method == 'POST':
#             book.delete()
#             return redirect('books:index')

#         return render(request, 'books/book_delete.html', {'book':book})


class BooksDeleteView(DeleteView):
    model = Books
    template_name = "books/book_delete.html"
    success_url =  reverse_lazy('books:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

       
    




   
    


