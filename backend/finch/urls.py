""" Finch App urls
"""
from django.urls import path
from finch import views

urlpatterns = [
    path('company/', views.company_detail, name='company-data'),
    path(
        'directory/',
        views.company_directory_list,
        name='company-directory-list'),
    path('individual/', views.individual_detail, name='individual-detail'),
    path(
        'employment/',
        views.individual_employment_detail,
        name='individual-employment-detail'),
]
