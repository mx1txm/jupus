from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, LegalRequest, DocumentAttachment
from .forms import ClientForm, LegalRequestForm, DocumentAttachmentForm, RegistrationForm
from django.contrib.auth import login, authenticate


#FOR CLIENT

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('legal_requests_dashboard')  # Redirect to your desired page after registration
    else:
        form = RegistrationForm()
    return render(request, 'jupusApp/register.html', {'form': form})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client/create_client.html', {'form': form})


def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/update_client.html', {'form': form, 'client': client})


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client/delete_client.html', {'client': client})

# FOR LEGAL REQUEST


def legal_request_list(request):
    legal_requests = LegalRequest.objects.all()
    return render(request, 'legal_request/legal_request_list.html', {'legal_requests': legal_requests})


def create_legal_request(request):
    if request.method == 'POST':
        form = LegalRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('legal_request_list')
    else:
        form = LegalRequestForm()
    return render(request, 'legal_request/create_legal_request.html', {'form': form})


def update_legal_request(request, legal_request_id):
    legal_request = get_object_or_404(LegalRequest, pk=legal_request_id)
    if request.method == 'POST':
        form = LegalRequestForm(request.POST, instance=legal_request)
        if form.is_valid():
            form.save()
            return redirect('legal_request_list')
    else:
        form = LegalRequestForm(instance=legal_request)
    return render(request, 'legal_request/update_legal_request.html', {'form': form, 'legal_request': legal_request})


def delete_legal_request(request, legal_request_id):
    legal_request = get_object_or_404(LegalRequest, pk=legal_request_id)
    if request.method == 'POST':
        legal_request.delete()
        return redirect('legal_request_list')
    return render(request, 'legal_request/delete_legal_request.html', {'legal_request': legal_request})


# FOR DocumentAttachment


def document_attachment_list(request):
    document_attachments = DocumentAttachment.objects.all()
    return render(request, 'document_attachment/document_attachment_list.html', {'document_attachments': document_attachments})


def create_document_attachment(request):
    if request.method == 'POST':
        form = DocumentAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_attachment_list')
    else:
        form = DocumentAttachmentForm()
    return render(request, 'document_attachment/create_document_attachment.html', {'form': form})


def update_document_attachment(request, document_attachment_id):
    document_attachment = get_object_or_404(DocumentAttachment, pk=document_attachment_id)
    if request.method == 'POST':
        form = DocumentAttachmentForm(request.POST, request.FILES, instance=document_attachment)
        if form.is_valid():
            form.save()
            return redirect('document_attachment_list')
    else:
        form = DocumentAttachmentForm(instance=document_attachment)
    return render(request, 'document_attachment/update_document_attachment.html', {'form': form, 'document_attachment': document_attachment})


def delete_document_attachment(request, document_attachment_id):
    document_attachment = get_object_or_404(DocumentAttachment, pk=document_attachment_id)
    if request.method == 'POST':
        document_attachment.delete()
        return redirect('document_attachment_list')
    return render(request, 'document_attachment/delete_document_attachment.html', {'document_attachment': document_attachment})


#DASHBOARD

def legal_requests_dashboard(request):
    legal_requests = LegalRequest.objects.all()
    context = {
        'legal_requests': legal_requests,
    }
    return render(request, 'jupusApp/legal_requests_dashboard.html', context)