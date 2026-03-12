from django.shortcuts import render, get_object_or_404
from .models import Shoe

def home(request):
    query = request.GET.get('q') # Search bar se text leta hai
    
    if query:
        # Filtered results (Latest first)
        shoes = (Shoe.objects.filter(name__icontains=query) | 
                 Shoe.objects.filter(brand__icontains=query)).order_by('-created_at')
    else:
        # Saare shoes (Latest first)
        shoes = Shoe.objects.all().order_by('-created_at')
    
    # Yahan 'index.html' aayega aur variable 'shoes' hoga
    return render(request, 'catalog/index.html', {'shoes': shoes})


def shoe_detail(request, pk):
    # Ek single shoe ki details ke liye
    shoe = get_object_or_404(Shoe, pk=pk)
    return render(request, 'catalog/shoe_detail.html', {'shoe': shoe})