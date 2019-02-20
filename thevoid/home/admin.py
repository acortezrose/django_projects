from django.contrib import admin
from .models import Comment

# Register your models here.

admin.site.site_header = "The Void Admin";
admin.site.site_title = "The Void Admin";

class CommentAdmin(admin.ModelAdmin):
	list_display = ['text', 'author', 'approved_comment']

admin.site.register(Comment, CommentAdmin)