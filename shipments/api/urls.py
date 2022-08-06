from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from . import views

urlpatterns = [
    path('', lambda _: redirect('swagger-ui')),
    path('shipment/', views.ShipmentList.as_view(), name='shipment-list'),
    path('shipment/<int:pk>/', views.ShipmentDetail.as_view(), name='shipment-detail'),
    path(
        'docs/',
        include(
            [
                path(
                    'openapi/', get_schema_view(
                        title='Shipments API',
                        description='API for Shipments',
                        version="1.0.0",
                    ),
                    name='openapi-schema',

                ),
                path(
                    'swagger/', TemplateView.as_view(
                        template_name='swagger-ui.html',
                        extra_context={'schema_url': 'openapi-schema.'},
                    ), name='swagger-ui',
                ),
            ]
        ),
    ),
]
