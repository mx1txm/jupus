from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class LegalRequest(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    case_description = models.TextField()
    case_type = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.case_type} - {self.status}"


class DocumentAttachment(models.Model):
    document = models.FileField(upload_to='attachments/')
    legal_request = models.ForeignKey(LegalRequest, on_delete=models.CASCADE)

    def __str__(self):
        return self.document.name
