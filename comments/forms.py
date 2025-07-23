from django.forms import ModelForm
from .models import Comment
from django import forms
from django.contrib.admin.widgets import BaseAdminDateWidget, BaseAdminTimeWidget

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields = ['text',]

class OtherWidget(forms.TextInput):
    class Media:
        css = {
            "all": ["other.css"]
        }
        js = ["other.js"]

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            "all": ["pretty.css"]
        }
        js = ["animations.js", "actions.js"]

class CustomTextInput(forms.TextInput):
    def __init__(self, icon='', *args, **kwargs):
        self.icon = icon
        super().__init__(*args, **kwargs)

    class Media:
        css = {"all": ["pretty.css"]}
        js = ["animations.js", "actions.js"]

    def render(self, name, value, attrs=None, renderer=None):
        original = super().render(name, value, attrs, renderer)
        if self.icon:
            return f'<div class="group"><img src="{self.icon}">{original}</div>'
        return original

class ContactForm(forms.Form):
    other = forms.CharField(widget=OtherWidget, help_text='Help text 1')
    calendar = forms.DateField(widget=BaseAdminTimeWidget, help_text='Help text 1')
    custom = forms.CharField(widget=CustomTextInput(icon='user.png'), help_text='Help text 1')