from django.contrib import admin
from models import * 

class PaintingAdmin(admin.ModelAdmin):
	date_hierarchy = "date_in"
	list_filter = ["technique", "author",]
	list_display = ["author", "title", "size", "reference"]
	search_fields = ["reference", "author", "title", "technique"]

admin.site.register(Painting, PaintingAdmin)
admin.site.register(Author)
admin.site.register(Technique)
