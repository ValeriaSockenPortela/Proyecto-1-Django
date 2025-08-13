from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from elements.models import Element, Category, Type
from comments.models import Comment
from .serializer import ElementReadOnlySerializer, ElementCreateUpdateDestroySerializer, CategorySerializer, TypeSerializer, CommentSerializer

class CreateUpdateDestroyViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, 
                                 mixins.UpdateModelMixin, viewsets.GenericViewSet):
    
    pass

class ElementReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Element.objects.all()
    serializer_class = ElementReadOnlySerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        print("Hola")
        queryset = Element.objects.all()
        serializer = ElementReadOnlySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def url(self, request):
        print("Hola2")
        queryset = Element.objects.get(slug=request.query_params['slug'])
        serializer = ElementReadOnlySerializer(queryset, many=False)
        return Response(serializer.data)

class ElementCreateUpdateDestroyViewSet(CreateUpdateDestroyViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementCreateUpdateDestroySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]