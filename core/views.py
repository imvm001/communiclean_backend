from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, ServiceBooking

class BookingAPI(APIView):
    def post(self, request):
        name = request.data.get('name')
        location = request.data.get('location')

        if not name or not location:
            return Response({'error': 'Missing data'}, status=400)

        customer, _ = Customer.objects.get_or_create(name=name, location=location)
        ServiceBooking.objects.create(customer=customer)

        return Response({'message': 'Booking stored successfully'}, status=status.HTTP_201_CREATED)