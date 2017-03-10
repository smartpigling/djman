# -*- coding: utf-8 -*-
from django.apps import AppConfig

__author__ = 'Xiaochuan Tang'


class AdminLteAppConfig(AppConfig):
    name = "core.adminlte"
    verbose_name = u"系统管理"

    def ready(self):
        import core.adminlte.serializers
        pass
