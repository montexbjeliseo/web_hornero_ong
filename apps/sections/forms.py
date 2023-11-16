from django import forms
from .models import SectionContent, SectionImage


class SectionContentForm(forms.ModelForm):
    class Meta:
        model = SectionContent
        fields = '__all__'


ImageFormSet = forms.inlineformset_factory(SectionContent, SectionImage, fields=[
                                           'image'], extra=3, can_delete=True)
