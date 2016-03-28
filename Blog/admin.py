from django.contrib import admin
from.models import Blog, UserProfile, Category, Comment

class CommentinLine(admin.TabularInline):
	model = Comment
	extra = 0
class BlogAdmin(admin.ModelAdmin):
    filedsets = [
        ('Blog Content', {'fields': ['title', 'category', 'creation_date']}),
        ('Body', {'fields': ['body', 'author']})
            ]
    list_display = ('title', 'body', 'creation_date')
    inlines = [CommentinLine]
    list_filter = ['creation_date']
    search_fields = ['title']

admin.site.register(Blog, BlogAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)