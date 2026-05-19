from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, validate_age


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    birth_date = forms.DateField(
        label='Дата рождения',
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'class': 'form-control',
                'placeholder': '25/12/1995',
                'type': 'text'
            }
        ),
        validators=[validate_age]
    )

    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '+375 (29) 123-45-67'
            }
        ),
        required=False,
        help_text='Формат: +375 (33) 123-45-67'
    )

    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'birth_date', 'phone_number', 'city', 'avatar', 'password1', 'password2']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')

        if not phone:
            return phone

        phone = phone.strip()
        if phone:
            from django.core.validators import RegexValidator
            validator = RegexValidator(regex=r'^\+375 \((25|29|33|44)\) \d{3}-\d{2}-\d{2}$', message='Номер телефона должен быть в формате: +375 (29) 123-45-67')
            validator(phone)

        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.save()

        profile = user.profile
        profile.birth_date = self.cleaned_data.get('birth_date')
        profile.phone_number = self.cleaned_data.get('phone_number')
        profile.city = self.cleaned_data.get('city')

        if self.cleaned_data.get('avatar'):
            profile.avatar = self.cleaned_data.get('avatar')

        profile.save()
        return user