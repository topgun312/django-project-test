import datetime

import pytz
from django import forms
from django.core.exceptions import ValidationError


class RobotAddForm(forms.Form):
    """
    Форма для валидации входящих данных в JSON формате и создания робота
    """

    jsonfield = forms.JSONField(max_length=1024, required=True, label="Формат JSON")

    def clean(self):
        json_data = self.cleaned_data.get("jsonfield")

        if not isinstance(json_data, dict):
            raise ValidationError(
                "Данные должны быть в формате JSON! Пример - '{'model':'R2','version':'D2','created':'2022-12-31 23:59:59'}'!"
            )

        model = json_data.get("model")
        version = json_data.get("version")
        created = json_data.get("created")

        if not isinstance(model, str) or len(model) > 2:
            raise ValidationError(
                "Модель робота должна быть строкой и иметь не более 2-х символов!"
            )

        if not isinstance(version, str) or len(version) > 2:
            raise ValidationError(
                "Версия робота должна быть строкой и иметь не более 2-х символов!"
            )

        if not isinstance(created, str):
            raise ValidationError(
                "Время создания робота должна быть строкой и иметь формат '2022-12-31 23:59:59'!"
            )

        try:
            current_datetime = datetime.datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValidationError(
                "Время создания робота должно иметь формат '2022-12-31 23:59:59'!"
            )

        serial = model + "-" + version
        json_data["serial"] = serial
        tz = pytz.timezone("UTC")
        current_date = tz.localize(current_datetime)
        json_data["created"] = current_date
        return json_data
