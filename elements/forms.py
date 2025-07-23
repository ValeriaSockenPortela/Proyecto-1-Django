from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import ModelForm
from django.utils.text import slugify

from .models import Type, Category, Element


# class ElementForm(ModelForm):
#     class Meta:
#         model = Element
#         fields = ['title', 'slug', 'description', 'price', 'type', 'category']

class ElementForm(forms.Form):
    def __init__(self, *args, **kargs):
        super().__init__( *args, **kargs)
        self.fields["description"].widget.attrs.update(size="40")
    title = forms.CharField(label='Title', max_length=255, min_length=3,
                            validators=[MinLengthValidator(3,message='Very short! (min %(limit_value)d) (current %(show_value)d)')],
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'data-id': '50'
                                }
                            ))

    slug = forms.SlugField(label='slug', max_length=255, min_length=3)
    description = forms.CharField(label='description', widget=forms.Textarea)
    price = forms.DecimalField(label='Price', decimal_places=2, max_digits=5, required=False)
    type = forms.ModelChoiceField(label='Type', queryset=Type.objects.all(), initial=1)
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(),
                                      widget=forms.RadioSelect)

    category.widget.attrs.update({'class':'special'})

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if Element.objects.filter(title=title).exists():
    #         raise ValidationError('Title already exists.')
    #     return title

    # def clean(self):
    #     form_data = self.cleaned_data
    #     if form_data['slug'] != slugify(form_data['title']):
    #         self._errors['slug'] = ["Slug do not match title"]
    #         del form_data['slug']
    #     return form_data
