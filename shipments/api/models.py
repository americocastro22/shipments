from django.core.validators import MinValueValidator
from django.db import models


class StatusChoices(models.TextChoices):
    CREATED = 'CREATED', 'Created'
    PLACED = 'PLACED', 'Placed'
    ON_DELIVERY = 'ON_DELIVERY', 'On_delivery'
    DELIVERED = 'DELIVERED', 'Delivered'


class TypeChoices(models.TextChoices):
    NORMAL = 'NORMAL', 'Normal'
    EXPRESS = 'EXPRESS', 'Express'


class Shipment(models.Model):
    origin = models.CharField(max_length=255, help_text='Shipment origin.')
    destination = models.CharField(max_length=255, help_text='Shipment destination.')
    weight = models.DecimalField(max_digits=7, decimal_places=3, validators=[MinValueValidator(0.001)],
                                 help_text='Shipment weight in Kg.')
    status = models.CharField(max_length=11, choices=StatusChoices.choices, default=StatusChoices.CREATED,
                              help_text='Shipment status.')
    type = models.CharField(max_length=7, choices=TypeChoices.choices, default=TypeChoices.NORMAL,
                            help_text='Shipment type.')
    complete = models.BooleanField(default=False, help_text='Indicates if shipment is completed.')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Date when the shipment was initiated.')
    updated_at = models.DateTimeField(auto_now=True, help_text='Date when the shipment was last updated.')
