from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def first_word(self):
		return self.text.split(" ")[0]		

	def rest_of_words(self):
		others = self.text.split(" ")[1:]
		return " ".join(others)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

	def get_absolute_url(self):  
        	return reverse('comments', args=[str(self.id)])
