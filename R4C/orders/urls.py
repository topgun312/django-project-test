from django.urls import path
from orders import views

urlpatterns = [
    path("add_order/", views.AddOrderView.as_view(), name="add_order"),
    path("error_buy/", views.ErrorBuyView.as_view(), name="error_buy"),
    path("success_buy/", views.SuccessBuyView.as_view(), name="success_buy"),
]
