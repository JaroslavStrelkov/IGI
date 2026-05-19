from django import forms
from django.utils.timezone import now
from .models import PromoCode

class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'discount_percent', 'valid_until', 'is_active']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SUMMER2026'}),
            'discount_percent': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 90}),
            'valid_until': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_discount_percent(self):
        percent = self.cleaned_data.get('discount_percent')
        if percent is not None:
            if percent < 1 or percent > 90:
                raise forms.ValidationError('Скидка должна быть от 1 до 90 процентов.')
        return percent

    def clean_valid_until(self):
        date = self.cleaned_data.get('valid_until')
        if date and date < now().date():
            raise forms.ValidationError('Дата действия промокода не может быть в прошлом!')
        return date

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if code:
            return code.strip().upper()
        return code