from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django_cookbook.settings import PROJECT_NAME


class IdeasAppConfig(AppConfig):
    name = PROJECT_NAME+".apps.ideas"
    verbose_name = _("Ideas")
