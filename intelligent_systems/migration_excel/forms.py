# forms.py

from django import forms
from django.core.validators import FileExtensionValidator

class CargarExcelForm(forms.Form):
    archivo_excel_estudiantes = forms.FileField(label="Indicadores ESTUDIANTES", required=True, validators=[FileExtensionValidator(allowed_extensions=[".xlsx", "xls"])])
    archivo_excel_profesores = forms.FileField(label="Indicadores PROFESORES", required=True, )


    class Meta:
        fields = ('archivo_excel_estudiantes', 'archivo_excel_profesores')

    def __init__(self, *args, **kwargs):
        super(CargarExcelForm, self).__init__(*args, **kwargs)

        self.fields['archivo_excel_estudiantes'].widget.attrs['class'] = 'mt-2 block w-full border-0 hover:border-blue-100 text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
        self.fields['archivo_excel_profesores'].widget.attrs['class'] = 'mt-2 block w-full border-0 hover:border-blue-100 text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'

