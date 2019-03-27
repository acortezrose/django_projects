
from ads.models import Ad

from django.views import View
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

from ads.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.forms import AdForm 

class AdListView(OwnerListView):
    def get(self, request):
    	model = Ad
    	template_name = "ad_list.html"
    	adlist = Ad.objects.all()
    	context = { 'adlist' : adlist }
    	return render(request, template_name, context)

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ad_detail.html"

class AdCreateView(OwnerCreateView):
	model = Ad
	template_name = "ad_form.html"
	fields = ['title', 'text']
    

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text']
    template_name = "ad_form.html"

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = "ad_delete.html"