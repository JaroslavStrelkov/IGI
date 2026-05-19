from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator)


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(90)])
    is_active = models.BooleanField(default=True)
    valid_until = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code