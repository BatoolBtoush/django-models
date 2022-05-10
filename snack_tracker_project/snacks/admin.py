from django.contrib import admin
from .models import Snack

# Register your models here.
# admin.site.register(Snack)

@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'purchaser', 'description', 'calories', 'sodium', 'fat', 'carbs', 'protein')
    list_filter = ('name', 'purchaser', 'description', 'calories', 'sodium', 'fat', 'carbs', 'protein')
    search_fields = ('name', 'purchaser', 'description', 'calories', 'sodium', 'fat', 'carbs', 'protein')
