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
    return


@api_view(['POST'])
def individual_detail():
    """
    List the details of a single employee's (individual) personal information.
    """
    return


@api_view(['POST'])
def individual_employment_detail():
    """ List the details of a single employee's company-related information.
    """
    return
# import json
# from urllib.parse import urljoin

# import requests
# from django.core.cache import cache
# # from django.http import HttpResponse, JsonResponse
# # from finch.utils import _get_data_from_sandbox_access_table
# # from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import SandboxAccess

# # from .serializers import SandboxAccessSerializer

# # Constants for views.py
# BASE_URL = 'https://sandbox.tryfinch.com/api/'
# CREATE_URL = urljoin(BASE_URL, 'sandbox/create')
# COMPANY_URL = urljoin(BASE_URL, 'employer/company')
# DIRECTORY_URL = urljoin(BASE_URL, 'employer/directoy')
# INDIVIDUAL_URL = urljoin(BASE_URL, 'employer/individual')
# EMPLOYMENT_URL = urljoin(BASE_URL, 'employer/employment')
# PRODUCT_SCOPES = ['company', 'directory', 'individual', 'employment']


# @api_view(['POST'])
# def create_sandbox_access(request):
#     """ This endpoint is called to get the access token for the specified
#     provider needed to make calls to other Sandbox API endpoints.
#     """
#     if request.method == 'POST':
#         try:
#             # 1. Check for cached access token.
#             sandbox_access_data = cache.get('sandbox_access_response', '')
#             # 2. If cached access token can't be found, check the database.
#             if not sandbox_access_data:
#                 provider_id = request.data.get('provider_id', '')
#                 database_response = _get_data_from_sandbox_access_table(
#                     provider_id)

#                 # If no valid record was found in the database, query the API to
#                 # create a new sandbox access token.
#                 if not database_response:
#                     sandbox_access_payload = {
#                         'provider_id': provider_id,
#                         'products': PRODUCT_SCOPES
#                     }
#                     sandbox_access_response = requests.post(
#                         CREATE_URL, json=sandbox_access_payload, timeout=10)

#                     if sandbox_access_response.status_code == 200:
#                         sandbox_access_response_data = (
#                             sandbox_access_response.json())

#                         # Create a new record in the database for the new
#                         # access token.
#                         sandbox_access = SandboxAccess(
#                             access_token=sandbox_access_response_data.get(
#                                 'access_token', ''),
#                             provider_name=sandbox_access_response_data.get(
#                                 'payroll_provider_id', ''),
#                             company_id=sandbox_access_response_data.get(
#                                 'company_id', ''),
#                             created_time=(
#                                 sandbox_access_response_data['sandbox_time']
#                                 .get('unix', 0))
#                         )
#                         sandbox_access.save()

#                         # Also add the response from the API call to the cache
#                         # for quick access.
#                         cache.set('sandbox_access_response',
#                                   sandbox_access_response_data)

#                         return Response({
#                             'message': ('Access token for Sandbox API created '
#                                         'successfully!'),
#                             'response_data': sandbox_access_response_data,
#                             'type': 'api'
#                         })
#                     return Response({
#                         'error': ("Failed to connect to the "
#                                   "Finch's POST /sandbox/create endpoint."),
#                         'response_data': False,
#                     })
#                 return Response({
#                     'message': ('Access token for Sandbox API located '
#                                 'in the database!'),
#                     'response_data': database_response,
#                     'type': 'database'
#                 })
#             return Response({
#                 'message': 'Access token for Sandbox API located in the cache!',
#                 'response_data': sandbox_access_data,
#                 'type': 'cache'
#             })
#         except json.JSONDecodeError as json_error:
#             return Response({
#                 'error': 'Invalid JSON data was returned.',
#                 'response_data': json_error
#             })
#     return Response({
#         'error': 'Invalid request made to the POST /access endpoint.',
#         'response_data': False
#     })


# @api_view(['GET'])
# def get_company_data(request):
#     """Gets company data"""
#     if request.method == 'GET':
#         try:
#             sandbox_access_data = requests.post(reverse('get_sandbox_access'))

#             access_token = sandbox_access_data.get('access_token', '')
#             headers = {'Authorization': f'Bearer {access_token}'}

#             company_response = requests.get(
#                 COMPANY_URL, headers=headers, timeout=10)
#             print(company_response.json)

#             if company_response.status_code == 200:
#                 company_response_data = company_response.json()

#                 return Response({
#                     'message': 'Company data retrieved successfully!',
#                     'response_data': company_response_data
#                 })
#             return Response({
#                 'error': ("Failed to connect to Finch's "
#                           "GET /employer/company endpoint."),
#                 'response_data': False
#             })
#         except json.JSONDecodeError as json_error:
#             return Response({
#                 'error': 'Invalid JSON data was returned.',
#                 'response_data': json_error
#             })
#     return Response({
#         'error': 'Invalid request made to the /company endpoint.',
#         'response_data': False
#     })


# @api_view(['GET'])
# def get_company_directory(request):
#     """Gets company directory"""
#     if request.method == 'GET':
#         try:
#             sandbox_access_data = get_sandbox_access(request)

#             access_token = sandbox_access_data.get('access_token', '')
#             headers = {f'Authorization: Bearer {access_token}'}

#             company_directory_response = request.get(
#                 DIRECTORY_URL, headers=headers, timeout=10)

#             if company_directory_response.status_code == 200:
#                 company_directory_response_data = (company_directory_response
#                                                    .json())

#                 return Response({
#                     'message': 'Company directory data retrieved successfully!',
#                     'response_data': company_directory_response_data
#                 })
#             return Response({
#                 'error': ("Failed to connect to Finch's "
#                           "GET /employer/directory endpoint."),
#                 'response_data': False
#             })
#         except json.JSONDecodeError as json_error:
#             return Response({
#                 'error': 'Invalid JSON data was returned.',
#                 'response_data': json_error
#             })
#     return Response({
#         'error': 'Invalid request made to the /directory endpoint.',
#         'response_data': False
#     })


# @api_view(['POST'])
# def get_individual_data(request):
#     """Gets individual data"""
#     if request.method == 'POST':
#         try:
#             sandbox_access_data = get_sandbox_access(request)

#             access_token = sandbox_access_data.get('access_token', '')
#             headers = {f'Authorization: Bearer {access_token}'}
#             individual_id = request.get('individual_id', '')
#             individual_payload = {
#                 requests: [
#                     {
#                         'individual_id': individual_id
#                     }
#                 ]
#             }

#             individual_response = request.post(
#                 INDIVIDUAL_URL,
#                 headers=headers,
#                 json=individual_payload,
#                 timeout=10)

#             if individual_response.status_code == 200:
#                 individual_response_data = individual_response.json()

#                 return Response({
#                     'message': 'Individual data retrieved successfully!',
#                     'response_data': individual_response_data
#                 })
#             return Response({
#                 'error': ("Failed to connect to Finch's "
#                           "POST /employer/individual endpoint."),
#                 'response_data': False
#             })
#         except json.JSONDecodeError as json_error:
#             return Response({
#                 'error': 'Invalid JSON data was returned.',
#                 'response_data': json_error
#             })
#     return Response({
#         'error': 'Invalid request made to the /directory endpoint.',
#         'response_data': False
#     })


# @api_view(['POST'])
# def get_individal_employment(request):
#     """Gets individual employment data"""
#     if request.method == 'POST':
#         try:
#             sandbox_access_data = get_sandbox_access(request)

#             access_token = sandbox_access_data.get('access_token', '')
#             headers = {f'Authorization: Bearer {access_token}'}
#             individual_id = request.get('individual_id', '')
#             individal_employment_payload = {
#                 requests: [
#                     {
#                         'individual_id': individual_id
#                     }
#                 ]
#             }

#             individal_employment_response = request.post(
#                 INDIVIDUAL_URL,
#                 headers=headers,
#                 json=individal_employment_payload,
#                 timeout=10)

#             if individal_employment_response.status_code == 200:
#                 individal_employment_response_data = (
#                     individal_employment_response.json())

#                 return Response({
#                     'message': ('Individual employment data retrieved '
#                                 'successfully!'),
#                     'response_data': individal_employment_response_data
#                 })
#             return Response({
#                 'error': ("Failed to connect to Finch's "
#                           "POST /employer/employment endpoint."),
#                 'response_data': False
#             })
#         except json.JSONDecodeError as json_error:
#             return Response({
#                 'error': 'Invalid JSON data was returned.',
#                 'response_data': json_error
#             })
#     return Response({
#         'error': 'Invalid request made to the POST /employment endpoint.',
#         'response_data': False
#     })


# class SandboxAccessView(viewsets.ModelViewSet):
#     serializer_class = SandboxAccessSerializer
#     queryset = SandboxAccess.objects.all()
