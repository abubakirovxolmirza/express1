from django.urls import path
from api.views.chat import ChatList, ChatDetail

from api.views.auth import (
    RegisterUserView, ListUsersView, 
    UserDetailView, CustomTokenObtainPairView )

from api.views.load import (
    TruckTagsDetailView, LoadListView, 
    LoadDetailView, DriverListView, 
    DriverDetailView, DriverTagsListView, 
    DriverTagsDetailView, TruckListView, 
    TrailerTagsDetailView, TruckDetailView, 
    TrailerListView, TrailerDetailView, 
    TrailerTagsListView, TruckTagsListView, 
    TrailerTagsDetailView, DispatcherListView, 
    DispatcherDetailView, DispatcherTagsListView, 
    DispatcherTagsDetailView, DispatcherTagsDetailView, 
    EmployeeListView, EmployeeDetailView, 
    EmployeeTagsDetailView, EmployeeTagsListView, 
    CustomerBrokerListView, CustomerBrokerDetailView, 
    CommoditiesListView, CommoditiesDetailView, OtherPayListView, 
    OtherPayDetailView, StopsListView, StopsDetailView, LoadTagsListView, 
    LoadTagsDetailView )

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register-user'),
    path('auth/users/', ListUsersView.as_view(), name='list-users'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),

    path('load/', LoadListView.as_view(), name='load-list'),
    path('load/<int:pk>/', LoadDetailView.as_view(), name='load-detail'),
    path('load/tags/', LoadTagsListView.as_view(), name='load-tags-list'),
    path('load/tags/<int:pk>/', LoadTagsDetailView.as_view(), name='load-tags-detail'),

    path('driver/', DriverListView.as_view(), name='driver-list'),
    path('driver/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
    path('driver/tags/', DriverTagsListView.as_view(), name='driver-tags-list'),
    path('driver/tags/<int:pk>/', DriverTagsDetailView.as_view(), name='driver-tags-detail'),

    path('truck/', TruckListView.as_view(), name='truck-list'),
    path('truck/<int:pk>/', TruckDetailView.as_view(), name='truck-detail'),
    path('truck/tags/', TruckTagsListView.as_view(), name='truck-tags-list'),
    path('truck/tags/<int:pk>/', TruckTagsDetailView.as_view(), name='truck-tags-detail'),

    path('trailer/', TrailerListView.as_view(), name='trailer-list'),
    path('trailer/<int:pk>/', TrailerDetailView.as_view(), name='trailer-detail'),
    path('trailer/tags/', TrailerTagsListView.as_view(), name='trailer-tags-list'),
    path('trailer/tags/<int:pk>/', TrailerTagsDetailView.as_view(), name='trailer-tags-detail'),

    path('dispatcher/', DispatcherListView.as_view(), name='dispatcher-list'),
    path('dispatcher/<int:pk>/', DispatcherDetailView.as_view(), name='dispatcher-detail'),
    path('dispatcher/tags/', DispatcherTagsListView.as_view(), name='dispatcher-tags-list'),
    path('dispatcher/tags/<int:pk>/', DispatcherTagsDetailView.as_view(), name='dispatcher-tags-detail'),

    path('employee/', EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/tags/', EmployeeTagsListView.as_view(), name='employee-tags-list'),
    path('employee/tags/<int:pk>/', EmployeeTagsDetailView.as_view(), name='employee-tags-detail'),
    
    path('customer_broker/', CustomerBrokerListView.as_view(), name='customer-broker-list'),
    path('customer_broker/<int:pk>/', CustomerBrokerDetailView.as_view(), name='customer-broker-detail'),

    path('commodities/', CommoditiesListView.as_view(), name='commodities-list'),
    path('commodities/<int:pk>/', CommoditiesDetailView.as_view(), name='commodities-detail'),
    
    path('other_pay/', OtherPayListView.as_view(), name='other-pay-list'),
    path('other_pay/<int:pk>/', OtherPayDetailView.as_view(), name='other-pay-detail'),

    path('stops/', StopsListView.as_view(), name='stops-list'),
    path('stops/<int:pk>/', StopsDetailView.as_view(), name='stops-detail'),

    path('load/tags/', LoadTagsListView.as_view(), name='load-tags-list'),
    path('load/tags/<int:pk>/', LoadTagsDetailView.as_view(), name='load-tags-detail'),

    path('chat/', ChatList.as_view()),
    path('chat/<int:pk>/', ChatDetail.as_view()),

]
