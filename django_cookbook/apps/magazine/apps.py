from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
<<<<<<< HEAD
from django_cookbook.settings import PROJECT_NAME


class MagazineConfig(AppConfig):
    name = PROJECT_NAME+'.apps.magazine'
    verbose_name = _('Magazine')

    def ready(self):
        from . import signals
