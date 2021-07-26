from django.contrib import admin
from .models import Register,Notes

# Register your models here.

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','user','contact','branch','role']


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id','user','uploadingdate','branch','subject','notesfile','filetype','desc','status']

