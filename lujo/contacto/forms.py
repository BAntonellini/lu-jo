from django import forms

OPCIONES_FORM = (
    ('masinfo', 'Más información'),
    ('cursos', 'Cursos')
)

"""
<option value="masinfo">Más información</option>
<option value="cursos">Cursos</option>
"""

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'form_name',
            'placeholder': 'Por favor ingresa el nombre *',
        }
    ), min_length=3, max_length=100)
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'form_lastname',
            'placeholder': 'Por favor ingresa tu apellido *',
        }
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Por favor ingresa tu email *',
        }
    ), min_length=3, max_length=150)
    tipoconsulta = forms.ChoiceField(label="Tipo de consulta", required = True, widget=forms.Select(
        attrs = {
            'class':'form-control',
            'id':'tipo_consulta',
        }
    ), choices = OPCIONES_FORM)
    mensaje = forms.CharField(label="Mensaje", required = True, widget = forms.Textarea(
        attrs = {
            'class': 'form-control',
            'id': 'form_message',
            'rows': 3,
        }
    ), min_length = 10, max_length = 1000)

