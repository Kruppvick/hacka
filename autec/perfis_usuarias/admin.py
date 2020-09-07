from django.contrib import admin
from .models import Perfil_usuaria
# Register your models here.

@admin.register(Perfil_usuaria)
class UsuariaReg(admin.ModelAdmin):
    list_display = ['id']