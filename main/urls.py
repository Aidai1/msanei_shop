from rest_framework import routers
from django.urls import path, include

from .views import CategoryListViewSet, CategoryDetailViewSet, UserListView, UserDetailView, ClothesListViewSet, RSSSubsViewSet, RedirectToTelegramBoView

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'category-list', CategoryListViewSet, basename='category-list')
router.register(r'category-detail', CategoryDetailViewSet, basename='category-detail')
router.register(r'clothes-list', ClothesListViewSet, basename='clothes-list')
router.register(r'rss-subs', RSSSubsViewSet, basename='rss-subs')




urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('redirect-to-telegram-bot/', RedirectToTelegramBoView.as_view(), name='redirect-to-telegram-bot'),
]