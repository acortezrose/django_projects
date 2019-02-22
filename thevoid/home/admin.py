from django.contrib import admin
from .models import Comment

# Register your models here.

admin.site.site_header = "The Void Admin";
admin.site.site_title = "The Void Admin";

def mark_approved(ModelAdmin, request, queryset):
	for comment in queryset:
		comment.approved_comment = True;
		comment.save()
mark_approved.short_description = "Mark as approved"

def mark_unapproved(ModelAdmin, request, queryset):
	for comment in queryset:
		comment.approved_comment = False;
		comment.save()
mark_unapproved.short_description = "Mark as unapproved"

class CommentAdmin(admin.ModelAdmin):
	list_display = ['text', 'approved_comment']
	list_filter = ['approved_comment']
	actions = [mark_approved, mark_unapproved, ]

admin.site.register(Comment, CommentAdmin)