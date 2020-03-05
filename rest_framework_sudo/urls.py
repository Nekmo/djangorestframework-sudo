from django.urls import path

from rest_framework_sudo.views import StatusView, UpdateStatusView

urlpatterns = [
    path('status/', StatusView.as_view()),
    path('update_status/', UpdateStatusView.as_view()),
]
