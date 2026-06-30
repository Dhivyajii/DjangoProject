from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from .forms import BookForm
# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request,'index.html',{'books':books})


def add_book(request):
    form=BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # print(request.POST)
            return redirect('index')
        else:
            form=BookForm()
    return render(request,'add_book.html',{'form':form})


def update_book(request, pk):
    # 1. Fetch the specific book or return a 404 error if it doesn't exist
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # 2. Pass request.POST AND the existing instance to the form
        form = BookForm(request.POST, request.FILES or None, instance=book)
        if form.is_valid():
            form.save() # This updates the existing record instead of creating a new one
            return redirect('index')
    else:
        # 3. Pre-fill the form with the book's current data
        form = BookForm(instance=book)
        
    return render(request, 'update_book.html', {'form': form, 'book': book})

# --- DELETE VIEW ---
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # If they confirmed the deletion (POST request), delete it
        book.delete()
        return redirect('index')
        
    # If they just clicked the link (GET request), show the confirmation page
    return render(request, 'delete_confirmation.html', {'book': book})



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')