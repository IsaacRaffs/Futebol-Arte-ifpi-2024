from django.contrib import admin
from core.models import Times

@admin.register(Times)
class AnimalAdmin(admin.ModelAdmin):
  list_display = ['nome', 'estado', 'cores', 'ano_de_fundação', 'mundial']
  list_filter = ['cores']
  search_fields = ['nome', 'cores', 'estado']


