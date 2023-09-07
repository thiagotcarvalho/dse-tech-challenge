"""Django views.py
"""

from urllib.parse import urljoin

import requests
from finch.utils import SandboxAccessToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# # Constants for views.py
BASE_URL = 'https://sandbox.tryfinch.com/api/'
COMPANY_URL = urljoin(BASE_URL, 'employer/company')
DIRECTORY_URL = urljoin(BASE_URL, 'employer/directory')
INDIVIDUAL_URL = urljoin(BASE_URL, 'employer/individual')
EMPLOYMENT_URL = urljoin(BASE_URL, 'employer/employment')


@api_view(['POST'])
def company_detail(request):
    """ List all details related to the company.
    """
    if request.method == 'POST':
        sandbox_access = SandboxAccessToken(
            request.data.get('provider_id', ''))
        access_data = sandbox_access.get_access_token()
        access_token = access_data['access_token']

        company_detail_response = requests.get(
            COMPANY_URL,
            headers={'Authorization': f'Bearer {access_token}'},
            timeout=5)
        print('DEBUG (/company/):', company_detail_response.json())

        if company_detail_response.status_code == 200:
            company_detail_json = company_detail_response.json()
            # TODO:
            # 1. Add response to cache
            #   1a. cache.set('company_detail_data_{provider_id}', company_detail_json)
            return Response(company_detail_json)
        return Response(status=company_detail_response.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def company_directory_list(request):
    """ List the company's directory of employees.
    """
    if request.method == 'POST':
        sandbox_access = SandboxAccessToken(
            request.data.get('provider_id', ''))
        access_data = sandbox_access.get_access_token()
        access_token = access_data['access_token']

        company_directory_list_response = requests.get(
            DIRECTORY_URL,
            headers={'Authorization': f'Bearer {access_token}'},
            timeout=5)
        print('DEBUG (/directory/):', company_directory_list_response.json())

        if company_directory_list_response.status_code == 200:
            company_directory_list_json = company_directory_list_response.json()
            # TODO:
            # 1. Add response to cache
            #   1a. cache.set('company_directory_list_data_{provider_id}', company_directory_list_json)
            return Response(company_directory_list_json)
        return Response(status=company_directory_list_response.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def individual_detail(request):
    """
    List the details of a single employee's (individual) personal information.
    """
    if request.method == 'POST':
        sandbox_access = SandboxAccessToken(
            request.data.get('provider_id', ''))
        access_data = sandbox_access.get_access_token()
        access_token = access_data['access_token']

        payload = {
            'requests': [
                {
                    'individual_id': request.data.get('individual_id', '')
                }
            ]
        }

        individual_detail_response = requests.get(
            INDIVIDUAL_URL,
            headers={'Authorization': f'Bearer {access_token}'},
            json=payload,
            timeout=5)
        print('DEBUG (/individual/):', individual_detail_response.json())

        if individual_detail_response.status_code == 200:
            individual_detail_json = individual_detail_response.json()
            # TODO:
            # 1. Add response to cache
            #   1a. cache.set('individual_detail_data_{provider_id}', individual_detail_json)
            return Response(individual_detail_json)
        return Response(status=individual_detail_response.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def individual_employment_detail(request):
    """ List the details of a single employee's company-related information.
    """
    if request.method == 'POST':
        sandbox_access = SandboxAccessToken(
            request.data.get('provider_id', ''))
        access_data = sandbox_access.get_access_token()
        print('access data', access_data)
        access_token = access_data['access_token']

        payload = {
            'requests': [
                {
                    'individual_id': request.data.get('individual_id', '')
                }
            ]
        }

        individual_employment_detail_response = requests.get(
            EMPLOYMENT_URL,
            headers={'Authorization': f'Bearer {access_token}'},
            json=payload,
            timeout=5)
        print('DEBUG (/employment/):',
              individual_employment_detail_response.json())

        if individual_employment_detail_response.status_code == 200:
            individual_employment_detail_json = (
                individual_employment_detail_response.json())
            # TODO:
            # 1. Add response to cache
            #   1a. cache.set('individual_employment_detail_data_{provider_id}', individual_employment_detail_json)
            return Response(individual_employment_detail_json)
        return Response(
            status=individual_employment_detail_response.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)
