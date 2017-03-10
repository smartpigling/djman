# -*- coding: utf-8 -*-

from django.apps import AppConfig

__author__ = 'Xiaochuan Tang'


class OrganizationAppConfig(AppConfig):
    name = "core.organization"
    verbose_name = u"组织机构"

    def ready(self):
        from rest_framework import serializers
        # import serializers
        pass


