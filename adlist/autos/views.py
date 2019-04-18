from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from autos.models import Auto, Comment
from autos.forms import CreateForm, CommentForm
from autos.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.
class AutoListView(OwnerListView):
	template = "autos/auto_list.html"

	def get(self, request):
		model = Auto
		autolist = Auto.objects.all()

		context = { 'autolist' : autolist }
		return render(request, self.template, context)


class AutoDetailView(OwnerDetailView):
	template = "autos/auto_detail.html"
	model = Auto

	def get(self, request, pk):
		auto = Auto.objects.get(id=pk)
		comments = Comment.objects.filter(auto=auto).order_by('-updated_at')
		comment_form = CommentForm()
		context = { 'auto' : auto, 'comments': comments, 'comment_form': comment_form }
		return render(request, self.template, context)


class AutoFormView(LoginRequiredMixin, View):
	template = "autos/auto_form.html"
	success_url = reverse_lazy('autos')

	def get(self, request, pk=None):
		if not pk :
			form = CreateForm()
		else:
			auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
			form = CreateForm(instance=auto)
		ctx = { 'form': form }
		return render(request, self.template, ctx)

	def post(self, request, pk=None):
		if not pk:
			form = CreateForm(request.POST, request.FILES or None)
		else:
			auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
			form = CreateForm(request.POST, request.FILES or None, instance=auto)

		if not form.is_valid() :
			ctx = {'form' : form}
			return render(request, self.template, ctx)

		# Adjust the model owner before saving
		auto = form.save(commit=False)
		auto.owner = self.request.user
		auto.save()
		return redirect(self.success_url)


class AutoDeleteView(OwnerDeleteView):
	model = Auto
	template_name = "autos/auto_delete.html"


class CommentCreateView(OwnerCreateView):
	def post(self, request, pk):
		f = get_object_or_404(Auto, id=pk)
		comment = Comment(text=request.POST['comment'], owner=request.user, auto=f)
		comment.save()
		return redirect(reverse_lazy('autos/auto_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
	model = Comment
	template_name = "autos/comment_delete.html"