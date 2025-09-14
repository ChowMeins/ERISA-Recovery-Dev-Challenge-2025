from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.claims_list, name='claims'),
    path("<int:claim_id>/detail/", views.claims_detail_modal, name='claim_detail'),
    path("<int:claim_id>/form/<str:form_type>", views.claims_form_modal, name='claims_form_modal'),
    path("<int:claim_id>/create_note", views.claims_create_note, name='claims_create_note'),
    path("<int:claim_id>/create_flag", views.claims_create_flag, name='claims_create_flag'),
    path("flags", views.claims_show_flags, name='flags')
]