from customers import views
from django.urls import path

urlpatterns = [
    path("add_customer/", views.AddCustomerView.as_view(), name="add_customer")
]
