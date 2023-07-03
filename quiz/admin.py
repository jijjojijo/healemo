from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from nested_admin.nested import NestedTabularInline, NestedModelAdmin

from .models import Question, Option, Quiz, Category, Rank, Result


class QuizAdminForm(forms.ModelForm):
    """Добавление ckeditor"""
    description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())

    class Meta:
        model = Quiz
        fields = '__all__'


class AnswerAdmin(NestedTabularInline):
    """NestedTabularInline для Option"""
    model = Option
    extra = 3


class QuestionAdmin(NestedTabularInline):
    """NestedTabularInline для Question"""
    model = Question
    inlines = [AnswerAdmin]
    extra = 3
    max_num = 20


class RankAdmin(NestedTabularInline):
    """NestedTabularInline для Rank"""
    model = Rank
    extra = 2
    max_num = 20


@admin.register(Quiz)
class QuizAdmin(NestedModelAdmin):
    """Quiz Admin"""
    model = Quiz
    form = QuizAdminForm

    list_display = ('title', 'category', 'draft', 'slug')
    list_editable = ('draft',)
    list_filter = ('draft',)
    ordering = ('draft',)
    list_per_page = 20
    search_fields = ('title', 'description')

    inlines = [QuestionAdmin, RankAdmin]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question Admin"""
    pass


@admin.register(Option)
class AnswerAdmin(admin.ModelAdmin):
    """Option Admin"""
    pass


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    """Result Admin"""
    pass
