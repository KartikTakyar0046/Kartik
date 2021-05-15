from django.shortcuts import render
from .models import Book,Gift
# Create your views here.
def home(request):
    gifts=Gift.objects.select_related('book')
    for g in gifts:
        print(g.book.price)
    return render(request,'index.html',context={'gifts':gifts})
