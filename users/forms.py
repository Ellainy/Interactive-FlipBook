from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import BaseUserCreationForm
from .models import User, Profile, Curso, Vinculo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['titulo'].widget.attrs['placeholder'] = 'Digite o nome do curso'

class VinculoForm(forms.ModelForm):
    class Meta:
        model = Vinculo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['vinculo'].widget.attrs['placeholder'] = 'Digite o nome do vínculo'

class CadastroForm(BaseUserCreationForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), empty_label="Selecione um curso")
    vinculo = forms.ModelChoiceField(queryset=Vinculo.objects.all(), empty_label="Selecione um vínculo")

    class Meta:
        model = User
        fields = ['username', 'email', 'curso', 'vinculo', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'primeiro_nome', 'ultimo_sobrenome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.fields['primeiro_nome'].label = 'Digite seu primeiro nome:'
        self.fields['ultimo_sobrenome'].label = 'Digite seu último sobrenome:'
        
        self.helper.layout = Layout(
            Row(
                Column('primeiro_nome', css_class='col-md-6'),
                Column('ultimo_sobrenome', css_class='col-md-6'),
                Column('avatar', css_class='col-md-12'),
                Submit('submit', 'Atualizar', css_class='col-md-12 btn btn-dark fundo-roxinho'),
            )
        )