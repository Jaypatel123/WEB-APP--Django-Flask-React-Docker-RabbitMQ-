from django.shortcuts import render
from rest_framework import viewsets

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        pass
    
    def create(self, request):
        pass
    
    def retrive(self, request, pk=None):
        pass
    
    def update(self, request, pk=None):
        pass
    
    def delete(self, request, pk=None):
        pass