#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""djman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django_js_reverse.views import urls_js
from core.adminlte.views import IndexView, ChangePasswordView, \
    ChangePasswordDoneView

# 基础 url
urlpatterns = [
    url('^page/change-password/$', ChangePasswordView.as_view(),
        name='change_password'),
    url('^page/change-password-done/$', ChangePasswordDoneView.as_view(),
        name='password_change_done'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', login_required(IndexView.as_view()), name='index'),

    url(r'^auth/', include("core.registration.urls",
                           namespace="registration")),

    url(r'^jsreverse/$', urls_js, name='js_reverse'),
]

# ===================== 自定义url映射 开始====================================
# 自定义url必须放在通用url的前面，将通用url覆盖掉
# Page url
urlpatterns += [
]
# API url
urlpatterns += [
    url(r'^api/v1/messageset/', include('core.messageset.urls_api',
                                        namespace='messageset_api')),
    # url(r'^api/v1/organization', include('organization.urls',
    # namespace='organization_api')),
]

# ===================== 自定义url映射 结束 ==================================

# 通用URL映射，必须放在最后
urlpatterns += [
    # 通用页面URL映射，必须放在最后
    url(r'^page/', include('core.adminlte.urls', namespace='adminlte')),
    url(r'^api/v1/', include('core.adminlte.urls_api',
                             namespace='adminlte_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
