from django import forms
from django.core import validators

from .models import Customer


class AddCustomerForm(forms.ModelForm):
    """
    Форма для создания клиента
    """

    email = forms.CharField(
        max_length=255,
        required=True,
        label="Email клиента",
        validators=[validators.EmailValidator(message="Не корректный email")],
    )

    class Meta:
        model = Customer
        fields = ("email",)
