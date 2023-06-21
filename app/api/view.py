from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from app.models import Product, Contract
from app.api.serializer import ManufacturerSerializer


class UniqueManufacturerView(APIView):
    def get(self, request, contract_id):
        contract = Contract.objects.filter(id=contract_id).first()
        if not contract:
            raise NotFound("Contract with this id does not exist.")

        products = (
            Product.objects
            .select_related('manufacturer', 'credit_application')
            .filter(credit_application=contract.credit_application.id)
            .all()
        )
        if not products:
            raise NotFound("Manufacture with this contract doest not exist.")

        manufacturers = {product.manufacturer for product in products}
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)
