
from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить

            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
                    print(count)
        # вызовом исключения ValidationError можно указать админке о наличие ошибки
        # таким образом объект не будет сохранен,
        # а пользователю выведется соответствующее сообщение об ошибке

        if count != 1:
            raise ValidationError('Тут всегда ошибка')

        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleScopeInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


admin.site.register(Tag)

