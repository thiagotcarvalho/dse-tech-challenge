"""Django models
"""
import uuid
from django.db import models


class SandboxAccess(models.Model):
    """ Model for SandboxAccess. """
    record_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    access_token = models.CharField(max_length=200)
    provider_name = models.CharField(max_length=25)
    company_id = models.CharField(max_length=50)
    created_time = models.BigIntegerField()
    latest_bool = models.BooleanField(default=True)

    class Meta:
        ordering = ('provider_name',)

    def __str__(self):
        return self.provider_name
