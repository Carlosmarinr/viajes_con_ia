from django.contrib import admin

from .models import Comment, Destination, Vote


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'author', 'featured', 'created_at')
    search_fields = ('title', 'location')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'created_at')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('destination', 'user', 'vote_type')
