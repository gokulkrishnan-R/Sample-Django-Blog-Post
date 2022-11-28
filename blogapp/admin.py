from django.contrib import admin
from .models import Posts,Comment
#@admin.register(Comment)

# Register your models here.
class PostAdmin(admin.ModelAdmin): #Customizing the admin panel
    list_display = ('title','status','posted_on')
    list_filter = [("title")]
    search_fields = ['title', 'content']

"""class CommentAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','image','posted_on')
    list_filter = [('title','posted_on')]
    search_fields = ['title', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
"""

admin.site.register(Posts,PostAdmin)
admin.site.register(Comment)