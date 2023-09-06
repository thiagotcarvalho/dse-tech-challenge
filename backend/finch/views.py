"""Django views.py
"""

import json
from urllib.parse import urljoin

import requests
from finch.utils import SandboxAccessToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# # Constants for views.py
BASE_URL = 'https://sandbox.tryfinch.com/api/'
COMPANY_URL = urljoin(BASE_URL, 'employer/company')
DIRECTORY_URL = urljoin(BASE_URL, 'employer/directoy')
INDIVIDUAL_URL = urljoin(BASE_URL, 'employer/individual')
EMPLOYMENT_URL = urljoin(BASE_URL, 'employer/employment')


@api_view(['GET'])
def company_detail(request):
    """ List all details related to the company.
    """
    if request.method == 'GET':
        sandbox_access = SandboxAccessToken(
            request.data.get('provider_id', ''))
        access_data = sandbox_access.get_access_token()
        access_token = access_data['access_token']

        company_detail_response = requests.get(
            COMPANY_URL,
            headers={'Authorization': f'Bearer {access_token}'},
            timeout=5
        )
        print('DEBUG:', company_detail_response.json())
        if company_detail_response.status_code == 200:
            company_detail_json = company_detail_response.json()
            # TODO:
            # 1. Add response to cache
            #   1a. cache.set('company_detail_data_{provider_id}', company_detai_json)
            return Response(company_detail_json)
        return Response(status=company_detail_response.status_code)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def company_directory_list():
    """ List the company's directory of employees.
    """
    return False


@api_view(['POST'])
def individual_detail():
    """
    List the details of a single employee's (individual) personal information.
    """
    return False


@api_view(['POST'])
def individual_employment_detail():
    """ List the details of a single employee's company-related information.
    """
    return False
