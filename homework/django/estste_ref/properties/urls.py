from django.urls import path
from properties.views import properties_list, property_detail, create_deal_request, owner_requests_list, approve_request, seeker_requests_list, reject_request
from properties.views import create_property, edit_property

app_name = 'properties' # namespace

urlpatterns = [
    path('', properties_list, name='list'),
    path('<int:prop_id>/', property_detail, name='detail'),
    path('<int:prop_id>/request/', create_deal_request, name='deal_request'),
    path('my-requests/', owner_requests_list, name='owner_requests'),
    path('my-srequests/', seeker_requests_list, name='seeker_requests'),
    path('request/<int:deal_request_id>/approve', approve_request, name='approve_request'),
    path('request/<int:deal_request_id>/reject', reject_request, name='reject_request'),
    path('property-create/', create_property, name='create_property'),
    path('property-edit/<int:prop_id>/', edit_property, name='edit_property'),
]
