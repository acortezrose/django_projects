
from ads.models import Ad, Comment

from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from ads.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.forms import CreateForm, CommentForm

class AdListView(OwnerListView):
    def get(self, request):
        model = Ad
        template_name = "ads/ad_list.html"
        adlist = Ad.objects.all()
        favorites = list()
        if request.user.is_authenticated:
            rows = request.user.favorite_ads.values('id')
            favorites = [ row['id'] for row in rows ]

        context = { 'adlist' : adlist, 'favorites': favorites }
        return render(request, template_name, context)

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"

    def get(self, request, pk) :
        ad = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : ad, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price', 'picture']
    template_name = "ads/ad_form.html"

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price', 'picture']
    template_name = "ads/ad_form.html"

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = "ads/ad_delete.html"


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=t)
        try:
            fav.save()  
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=t).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()

class PicFormView(LoginRequiredMixin, View):
    template = 'ads/ad_form.html'
    success_url = reverse_lazy('ads')
    def get(self, request, pk=None) :
        if not pk :
            form = CreateForm()
        else:
            pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
            form = CreateForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model owner before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

def stream_file(request, pk) :
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response

class CommentCreateView(OwnerCreateView):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment_form = CommentForm(request.POST)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=f)
        comment.save()
        return redirect(reverse_lazy('ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"