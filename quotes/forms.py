from django import forms

from .models import Quote


class QuoteForm(forms.ModelForm):
    author = forms.CharField(required=False, label='Вкажіть існуючого автора')

    class Meta:
        model = Quote
        fields = ['author', 'quote', 'tags']
        widgets = {
            'quote': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введіть текст цитати'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Введіть теги через кому'}),
        }

