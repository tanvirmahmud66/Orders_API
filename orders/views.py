from rest_framework import status, generics 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class OrderListCreate(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of all orders",
        responses={200: OrderSerializer(many=True)}
    )
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=OrderSerializer,
        responses={201: OrderSerializer, 400: "Bad Request"}
    )
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderDetail(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve an order by its ID",
        responses={200: OrderSerializer, 404: "Not Found"}
    )
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    @swagger_auto_schema(
        operation_description="Update an existing order",
        request_body=OrderSerializer,
        responses={200: OrderSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Partially update an existing order",
        request_body=OrderSerializer,
        responses={200: OrderSerializer, 400: "Bad Request", 404: "Not Found"}
    )
    def patch(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an order by its ID",
        responses={204: "No Content", 404: "Not Found"}
    )
    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
