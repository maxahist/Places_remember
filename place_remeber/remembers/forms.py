from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Remember

class RememberForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = ('name', 'description', 'location')
        widgets = {'location': LeafletWidget()}