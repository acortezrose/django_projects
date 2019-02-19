from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from home.models import Comment

class CommentForm(forms.ModelForm):
#	author = forms.CharField()
#	text = forms.CharField()
	class Meta:
		model = Comment
		fields = ('author', 'text',)
		labels = {'author': "Name", 'text': "What's been on your mind?",}
		widgets = {
			'author': forms.TextInput(attrs={'placeholder': 'anonymous'}),
			'text': forms.Textarea(attrs={'placeholder': 'shout something into the void'}),
		}

