from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from home.models import Comment
from home.forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
	comment_list = Comment.objects.all()
	paginator = Paginator(comment_list, 10)
	page = request.GET.get('page')
	comments = paginator.get_page(page)

	context = {
		"comments": comments,
	}

	return render(request, 'index.html', context=context)

from django.views import generic

def SubmitView(request):
	form = CommentForm(request.POST)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.save()
		return redirect('index')
	else:
		form = CommentForm()

	context = {
		'form': form,
	}

	return render(request, 'submit.html', context=context)

def about(request):
	return render(request, 'about.html', {})
