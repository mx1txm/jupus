"""
URL configuration for jupProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jupusApp import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include
from django.views.generic import RedirectView  # Import the redirect function



urlpatterns = [
    path('legal-requests/', views.legal_requests_dashboard, name='legal_requests_dashboard'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='jupusApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='jupusApp/logout.html'), name='logout'),
    path('register/', views.register, name='register'),    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/<int:client_id>/update/', views.update_client, name='update_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),

#   URLs for LegalRequest views
    path('legal-requests/list/', views.legal_request_list, name='legal_request_list'),
    path('legal-requests/create/', views.create_legal_request, name='create_legal_request'),
    path('legal-requests/<int:legal_request_id>/update/', views.update_legal_request, name='update_legal_request'),
    path('legal-requests/<int:legal_request_id>/delete/', views.delete_legal_request, name='delete_legal_request'),

#   URLs for DocumentAttachment views
    path('document-attachments/list/', views.document_attachment_list, name='document_attachment_list'),
    path('document-attachments/create/', views.create_document_attachment, name='create_document_attachment'),
    path('document-attachments/<int:document_attachment_id>/update/', views.update_document_attachment, name='update_document_attachment'),
    path('document-attachments/<int:document_attachment_id>/delete/', views.delete_document_attachment, name='delete_document_attachment'),
]



