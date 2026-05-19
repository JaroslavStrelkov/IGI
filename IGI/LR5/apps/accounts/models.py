from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date


def validate_age(birth_date):
    if birth_date is None:
        return
    
    today = date.today()
    age = (today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))
    if age < 18:
        raise ValidationError('Вам должно быть минимум 18 лет для регистрации. Auf Wiedersehen!')


class Profile(models.Model):
    ROLE_CHOICES = [('customer', 'Клиент'), ('employee', 'Сотрудник'), ('admin', 'Администратор'),]

    phone_regex = RegexValidator(regex=r'^\+375 \((25|29|33|44)\) \d{3}-\d{2}-\d{2}$', message='Номер должен быть в формате: +375 (25/29/33/44) 123-45-67')
    phone_number = models.CharField(max_length=19, validators=[phone_regex], unique=True, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    birth_date = models.DateField(null=True, blank=True, validators=[validate_age])
    city = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username