from django.views.generic import ListView
from .models import *

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'