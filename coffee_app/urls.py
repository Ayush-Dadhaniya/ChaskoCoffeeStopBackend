from django.urls import path
from .views import RegisterView, LoginView, MenuItemList, ReviewList, SubscriptionCreate

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('menu/', MenuItemList.as_view(), name='menu-list'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('subscriptions/', SubscriptionCreate.as_view(), name='subscription'),
]
