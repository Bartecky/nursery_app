"""Nursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from NurseryApp.views import (
    NurseryLoginView,
    NurseryLogoutView,
    SignupView,
    MainPageView,
    ChildCreateView,
    ChildDetailView,
    ChildUpdateView,
    ChildDeleteView,
    GroupCreateView,
    GroupDetailView,
    GroupUpdateView,
    GroupDeleteView,
    GroupListView,
    TeacherCreateView,
    TeacherDetailView,
    TeacherUpdateView,
    TeacherDeleteView,
    TeacherListView

)

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', NurseryLoginView.as_view(), name='login-view'),
    url(r'^logout/$', NurseryLogoutView.as_view(), name='logout-view'),
    url(r'^signup/$', SignupView.as_view(), name='signup-view'),
    url(r'^main/$', MainPageView.as_view(), name='main-view'),
    #
    url(r'^parent/(?P<pk>(\d)+)/add_child/$', ChildCreateView.as_view(), name='child-create-view'),
    url(r'^child/detail/(?P<pk>(\d)+)/$', ChildDetailView.as_view(), name='child-detail-view'),
    url(r'^child/update/(?P<pk>(\d)+)/$', ChildUpdateView.as_view(), name='child-update-view'),
    url(r'^child/delete/(?P<pk>(\d)+)/$', ChildDeleteView.as_view(), name='child-delete-view'),
    url(r'^add_group/$', GroupCreateView.as_view(), name='group-create-view'),
    url(r'^group/detail/(?P<pk>(\d)+)/$', GroupDetailView.as_view(), name='group-detail-view'),
    url(r'^group/update/(?P<pk>(\d)+)/$', GroupUpdateView.as_view(), name='group-update-view'),
    url(r'^group/delete/(?P<pk>(\d)+)/$', GroupDeleteView.as_view(), name='group-delete-view'),
    url(r'^group/list/$', GroupListView.as_view(), name='group-list-view'),
    url(r'^add_teacher/$', TeacherCreateView.as_view(), name='teacher-create-view'),
    url(r'^teacher/detail/(?P<pk>(\d)+)/$', TeacherDetailView.as_view(), name='teacher-detail-view'),
    url(r'^teacher/update/(?P<pk>(\d)+)/$', TeacherUpdateView.as_view(), name='teacher-update-view'),
    url(r'^teacher/delete/(?P<pk>(\d)+)/$', TeacherDeleteView.as_view(), name='teacher-delete-view'),
    url(r'^teacher/list/$', TeacherListView.as_view(), name='teacher-list-view'),


]
