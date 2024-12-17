from typing import Any

from .utils import menu


def get_menu_context(request: Any) -> Any:
    """
    Фунцкия для создания шаблонного контекстного процессора для отображения меню сайта
    """
    return {"mainmenu": menu}
