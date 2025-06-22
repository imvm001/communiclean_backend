from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer

class BookingAPI(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            location = request.data.get('location')

            if not name or not location:
                return Response(
                    {"message": "Both name and location are required."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            Customer.objects.create(name=name, location=location)

            return Response(
                {"message": "Booking submitted successfully!"},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"message": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )