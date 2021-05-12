from django.shortcuts import render,redirect,reverse
import random
from django.contrib import *
from django.contrib.auth.models import User
from django.views.generic import (DetailView,FormView,ListView,TemplateView,UpdateView)
from django.contrib.auth.decorators import login_required
from .models import Item,itemHistory,Payment,Category
# Create your views here.


def home(request):
    return render(request,'Home.html')

def Aboutus(request):
    return render(request,'Aboutus.html')

def Listitem(request):
    cat = request.GET['category']
    if cat == "Colourful":
        title = "COLOURFUL"
        some_colour = Category.objects.get(category="Colourful")
        Item_colour = Item.objects.all().filter(category=some_colour).order_by('-name')
        context = {'Item': Item_colour,'title' : title}   
 
    else:
        title = "EARTH TONES"
        some_Earthtones = Category.objects.get(category="Earthtones")
        Item_Earthtones = Item.objects.all().filter(category=some_Earthtones).order_by('-name')
        context = {'Item': Item_Earthtones,'title' : title}
        
    return render(request,'Category.html',context=context)

def Random(request):
    return render(request,'Random.html')

def Open(request):
    tone = request.GET['Tone']
    if tone == "Earthtones":
        return render(request,'OpenEarthtone.html')
    elif tone == "Colourful":
        return render(request,'OpenColourful.html')

def Detail(request):
    type=request.GET['type']
    if request.user.is_authenticated:
        if type == "Earthtones":
            some_Earthtones = Category.objects.get(category="Earthtones")
            Item_Earthtones = list(Item.objects.all().filter(category=some_Earthtones))
            randomItemE = random.sample(Item_Earthtones,1)
            context = {'Item': randomItemE}
        elif type == "Colourful":
            some_Colourful = Category.objects.get(category="Colourful")
            Item_Colourful = list(Item.objects.all().filter(category=some_Colourful))
            randomItemC = random.sample(Item_Colourful,1)
            context = {'Item': randomItemC}
        return render(request,'Detail.html',context=context)
    else:
        messages.info(request,"Login Before Random please") 
        return redirect('/Login')
        

@login_required(login_url='Login')
def Payment(request):
    if request.method == "POST":
        pass
    return render(request,'Payment.html')


class SearchItemListView(ListView):
    template_name = "Colourful.html"
    model = Item

    def get_queryset(self):
        queryset = super(SearchItemListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            item_by_name = queryset.filter(name__icontains=q)
            item_by_category = queryset.filter(category__icontains=q)
            return item_by_name | item_by_category
        return queryset












# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "Detail.html"

#     def get_success_url(self):
#         return reverse('Detail', kwargs={'slug': self.object.slug})