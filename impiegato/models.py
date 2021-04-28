from django.db import models

class Impiegato(models.Model):
    emplyee_regNo = models.TextField(unique=True)
    emplyee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)