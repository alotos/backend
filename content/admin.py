from django import forms
from django.contrib import admin
from .models import MainPage
from .models import ContactsPage
from .models import Slider
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = MainPage
        fields = '__all__'

class ContactsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ContactsPage
        fields = '__all__'

admin.site.register(MainPage)
admin.site.register(ContactsPage)
admin.site.register(Slider)