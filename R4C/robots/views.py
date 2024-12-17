from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView
from robots.forms import RobotAddForm
from robots.models import Robot


class AddRobotInfo(FormView):
    """
    Представление для добавления роботов в БД
    """

    form_class = RobotAddForm
    template_name = "robots/robot_add.html"
    success_url = reverse_lazy("robot_list")

    def form_valid(self, form):
        Robot.objects.create(**form.cleaned_data)
        return redirect("robot_list")


class MainPage(TemplateView):
    """
    Представление для отображения главной страницы
    """

    template_name = "robots/main.html"


class RobotList(ListView):
    """
    Представление для получения списка роботов
    """

    template_name = "robots/robot_list.html"
    context_object_name = "robots"

    def get_queryset(self):
        return Robot.objects.all()
