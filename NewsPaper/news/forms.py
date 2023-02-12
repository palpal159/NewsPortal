from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    text_post = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['header_post',
                  'text_post',
                  'category']

    def clean(self):
        cleaned_data = super().clean()
        header_post = cleaned_data.get("header_post")
        text_post = cleaned_data.get("text_post")

        if header_post == text_post:
            raise ValidationError(
                "Текст поста не должен быть идентичен заголовку."
            )

        return cleaned_data
