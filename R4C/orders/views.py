from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from robots.models import Robot

from .forms import AddOrderForm


class AddOrderView(CreateView):
    """
    Представление для создания заказа
    """

    form_class = AddOrderForm
    template_name = "orders/order_add.html"
    success_url = reverse_lazy("robot_list")

    def form_valid(self, form):
        form.save()
        robot_serial = form.cleaned_data["robot_serial"]
        if Robot.objects.filter(serial=robot_serial).count() > 0:
            return redirect("success_buy")
        else:
            return redirect("error_buy")


class ErrorBuyView(TemplateView):
    """
    Представление для отображения страницы отложенного заказа
    """

    template_name = "orders/error_buy.html"


class SuccessBuyView(TemplateView):
    """
    Представление для отображения страницы успешного заказа
    """

    template_name = "orders/success_buy.html"
