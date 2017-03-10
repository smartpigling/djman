#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
from core.adminlte.models import Permission, Menu
from core.adminlte.constants import UsableStatus

__author__ = 'Xiaochuan Tang'


class ApiPermissionCheck(MiddlewareMixin):

    def process_request(self, request):
        if not request.user.is_superuser and \
                request.path_info.startswith('/api/'):
            # todo: cache
            permissions = Permission.objects.filter(
                group__in=request.user.groups.all()
            )
            resources = []
            for p in permissions:
                resources.append(p.resources.values_list('url', flat=True))

            if request.path_info not in resources:
                return HttpResponse(status=403)
        pass


class MenuMiddleware(MiddlewareMixin):

    def process_template_response(self, request, response):
        # todo: cache
        if request.path_info.startswith('/page/') or request.path_info == '/':
            if request.user.is_superuser:
                page_menus = Menu.objects.filter(status=UsableStatus.USABLE)
            else:
                groups = request.user.groups.all()
                permission = Permission.objects.filter(
                    group__in=groups
                ).first()
                # page_menus = permission.menus.all()
                try:
                    page_menus = permission.menus.all()
                except:
                    page_menus = None
            response.context_data['page_menus'] = page_menus
        return response