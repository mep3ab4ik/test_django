from django.urls import path
from app.api.view import UniqueManufacturerView

urlpatterns = [
    path('unique-manufacturer/<int:contract_id>/', UniqueManufacturerView.as_view(), name='unique_manufacturer'),
]
