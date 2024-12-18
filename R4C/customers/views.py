from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AddCustomerForm


class AddCustomerView(CreateView):
    """
    Представление для создания клиента
    """

    form_class = AddCustomerForm
    template_name = "customers/add_customer.html"
    success_url = reverse_lazy("robot_list")
