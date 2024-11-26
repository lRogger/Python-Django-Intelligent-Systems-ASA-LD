# forms.py

from django import forms

class CargarExcelForm(forms.Form):
    archivo_excel = forms.FileField(label="Selecciona un archivo Excel", required=True)


    class Meta:
        fields = ('migracion')
