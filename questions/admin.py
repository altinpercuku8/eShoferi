from django.contrib import admin
from .models import Questions, Anwser
# Register your models here.

class AnwserInLine(admin.TabularInline):
    model = Anwser

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnwserInLine]

admin.site.register(Questions , QuestionAdmin)
admin.site.register(Anwser)
