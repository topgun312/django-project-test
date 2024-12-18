from customers.models import Customer
from django import forms
from django.core.exceptions import ValidationError
from django.db import ProgrammingError
from robots.models import Robot

from .models import Order


class AddOrderForm(forms.ModelForm):
    """
    Форма для создания заказа
    """

    robot_serial = forms.CharField(max_length=5, required=True, label="Серия робота")
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        to_field_name="email",
        empty_label="Email не выбран",
        label="Email",
    )

    class Meta:
        model = Order
        fields = ("robot_serial", "customer")

    def clean(self):
        robot_serial = self.cleaned_data.get("robot_serial")
        if not isinstance(robot_serial, str) or len(robot_serial) != 5:
            raise ValidationError(
                "Серия робота должна быть строкой и иметь 5 символов. Пример - 'R4-S4'!"
            )
