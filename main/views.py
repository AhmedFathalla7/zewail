from django.shortcuts import render
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    all_products = Product.objects.all()
    filters = Product.objects.filter(category__name="الفلاتر")
    spare_parts = Product.objects.filter(category__name="قطع الغيار")

    return render(request, "index.html", {
        "categories": categories,
        "all_products": all_products,
        "filters": filters,
        "spare_parts": spare_parts,
    })
