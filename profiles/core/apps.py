from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CoreConfig(AppConfig):
    name = 'profiles.core'
    verbose_name = _('core')

    def ready(self):
        import profiles.core.signals  # noqa