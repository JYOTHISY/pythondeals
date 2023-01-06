from django.shortcuts import render,redirect
from django.http import HttpResponse
from productapp.forms import ProductForm
from productapp.models import Product
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.




def add(request):
    productlist = Product.objects.all()
    form =ProductForm()
    if request.method == 'POST':
        form =ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'productapp/home.html',{'productlist': productlist,'form':form})


def search_product(request):
    """ search function  """
    productlist=[]
    if 'query' in request.GET:
        query = request.GET['query']
        productlist=Product.objects.filter(productName__icontains=query)

        #context={'productlist': productlist}


    return render(request, 'productapp/search.html', {'productlist': productlist} )



