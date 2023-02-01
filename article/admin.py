""" docs """
from django.contrib import admin
from .models import Article


# Regular method
# admin.site.register(Article)

# Beta method
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Indicate model fields to display in admin dashboard.
    Notice search fileds to search artcles in db
    """

    list_display = ("title", "published", "author")
    date_hierarchy = "published"
    search_fields = ("title", "description")
