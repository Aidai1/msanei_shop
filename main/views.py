from rest_framework import viewsets, mixins, generics, permissions
from django.shortcuts import render 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import Clothes, Category, Brand, ClothesSize, ClothesColor, ClothesInStock, RSSSubs
from .serializers import CategoryListSerializer, CategoryDetailSerializer, UserSerializer, ClothesListSerializer, ClothesSizeSerializer, ClothesColorSerializer, ClothesInStockSerializer, RSSSubsSerializer
from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsClotherOwnerOrReadOnly

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly, )


class CategoryListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class ClothesListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializer
    permission_classes = (IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class ClothesSizeListViewSet(viewsets.ModelViewSet):
    queryset = ClothesSize.objects.all()
    serializer_class = ClothesSizeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ClothesColorListViewSet(viewsets.ModelViewSet):
    queryset = ClothesColor.objects.all()
    serializer_class = ClothesColorSerializer


class ClothesInStockListViewSet(viewsets.ModelViewSet):
    queryset = ClothesInStock.objects.all()
    serializer_class = ClothesInStockSerializer
    permission_classes = (IsClotherOwnerOrReadOnly,)


class RSSSubsViewSet(viewsets.ModelViewSet):
    queryset = RSSSubs.objects.all()
    serializer_class = RSSSubsSerializer
    permission_classes = (permissions.AllowAny,)


class RedirectToTelegramBoView(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(redirect_to='https://t.me/yrk_rysyaBOT')
