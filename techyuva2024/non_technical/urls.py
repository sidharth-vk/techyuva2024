from django.urls import path
from .views import *

urlpatterns = [
    path('Non-Technical-Events',all_nontechnical_events,name="all_nontechnical_events"),
    path('Non-Technical-Events/<pk>',non_event_detail_page,name="non_event_detail_page"),
    path('Non-Technical-Events/register/<pk>',non_event_register_page,name="non_event_register_page"),
    path('Non-Technical-Events/proof/<pk>',nonproof,name="nonproof")
]
