from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ['pub_date',]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)