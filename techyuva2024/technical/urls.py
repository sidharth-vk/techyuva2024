from django.urls import path
from .views import *

urlpatterns = [
    path('Technical-Events',all_technical_events,name="all_technical_events"),
    path('Technical-Events/<pk>',event_detail_page,name="event_detail_page"),
    path('Technical-Events/register/<pk>',event_register_page,name="event_register_page"),
    path('Technical-Events/proof/<pk>',proof,name="proof")
]
