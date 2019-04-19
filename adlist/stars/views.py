from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from stars.models import Star, Comment
from stars.forms import CreateForm, CommentForm
from stars.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.
class StarListView(OwnerListView):
	template = "stars/star_list.html"

	def get(self, request):
		model = Star
		starlist = Star.objects.all()

		context = { 'starlist' : starlist }
		return render(request, self.template, context)


class StarDetailView(OwnerDetailView):
	template = "stars/star_detail.html"
	model = Star

	def get(self, request, pk):
		star = Star.objects.get(id=pk)
		comments = Comment.objects.filter(star=star).order_by('-updated_at')
		comment_form = CommentForm()
		context = { 'star' : star, 'comments': comments, 'comment_form': comment_form }
		return render(request, self.template, context)


class StarFormView(LoginRequiredMixin, View):
	template = "stars/star_form.html"
	success_url = reverse_lazy('stars')

	def get(self, request, pk=None):
		if not pk :
			form = CreateForm()
		else:
			star = get_object_or_404(Star, id=pk, owner=self.request.user)
			form = CreateForm(instance=star)
		ctx = { 'form': form }
		return render(request, self.template, ctx)

	def post(self, request, pk=None):
		if not pk:
			form = CreateForm(request.POST, request.FILES or None)
		else:
			star = get_object_or_404(star, id=pk, owner=self.request.user)
			form = CreateForm(request.POST, request.FILES or None, instance=star)

		if not form.is_valid() :
			ctx = {'form' : form}
			return render(request, self.template, ctx)

		# Adjust the model owner before saving
		star = form.save(commit=False)
		star.owner = self.request.user
		star.save()
		return redirect(self.success_url)


class StarDeleteView(OwnerDeleteView):
	model = Star
	template_name = "stars/star_delete.html"


class CommentCreateView(OwnerCreateView):
	def post(self, request, pk):
		f = get_object_or_404(Star, id=pk)
		comment = Comment(text=request.POST['comment'], owner=request.user, star=f)
		comment.save()
		return redirect(reverse_lazy('star_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
	model = Comment
	template_name = "stars/comment_delete.html"