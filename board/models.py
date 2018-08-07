from django.db import models
from djmoney.models.validators import MinMoneyValidator

from authentication.models import User

from djmoney.models.fields import MoneyField

Type_Choices = (
    ('One-on-One', 'one-on-one'),
    ('E-lessons', 'online'),
)


class Service(models.Model):
    Title = models.CharField(max_length=30)
    type = models.CharField(max_length=60, choices=Type_Choices, default='None', blank=True)
    description = models.TextField()
    rate_per_hour = MoneyField(max_digits=19, decimal_places=4, default_currency='KES', validators=[MinMoneyValidator(1)])
    user = models.ForeignKey(User)


