"""Django utility functions.
"""
from datetime import datetime, timedelta

import requests
from django.core.cache import cache
from finch.models import SandboxAccess
from finch.serializers import SandboxAccessSerializer
from rest_framework import status
from rest_framework.response import Response


class SandboxAccessToken:
    """ Helper class to get/create an access token for Finch's Sandbox API
    """

    def __init__(self, provider_id) -> None:
        self.url = 'https://sandbox.tryfinch.com/api/sandbox/create'
        self.provider_id = provider_id
        self.product_scopes = ['company', 'directory',
                               'individual', 'employment']

    def get_unix_timestamp(self, date):
        """ Turns a datetime date into a millisecond timestamp.
        """
        return date.timestamp() * 1000

    def add_new_database_record(self, api_data):
        """ Adds a new access token record to the database.
        """
        db_data = {
            'provider_id': api_data.get('payroll_provider_id', ''),
            'company_id': api_data.get('company_id', ''),
            'access_token': api_data.get('access_token', ''),
            'created_time': api_data['sandbox_time'].get('unix', 0)
        }
        serializer = SandboxAccessSerializer(data=db_data)
        print('serializer', serializer)
        if serializer.is_valid():
            print('did this work?', serializer)
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_from_database(self):
        """ Checks for Finch Sandbox API access token in the database.
        """
        # Firstly, check if database has any records.
        try:
            has_records = SandboxAccess.objects.exists()
            if not has_records:
                return False
        except SandboxAccess.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # If there are records, check to see if it's valid.
        # Validity criteria:
        #   1. latest_bool == True.
        #   2. Must match provider_id.
        #   3. Must have been created no later than 23 hours ago
        #      (sandbox environments expire after 24 hours).

        # Get the timestamp of today's and yesterday's date
        ms_today = self.get_unix_timestamp(datetime.now())
        ms_yesterday = self.get_unix_timestamp(
            (datetime.now() - timedelta(hours=23)))

        valid_access = SandboxAccess.objects.filter(
            latest_bool=True, provider_name=self.provider_id,
            created_time__gte=ms_yesterday, created_time__lte=ms_today)
        # If there are no records that meet the criteria,
        # we must update the most recent record's latest_bool to False.
        # There should always be one record with a latest_bool of True
        # while all others are False
        if not valid_access:
            record_to_update = SandboxAccess.objects.filter(
                latest_bool=True, provider_name=self.provider_id)
            serializer = SandboxAccessSerializer(
                record_to_update, data={'latest_bool': False})

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # If the record exists, return it.
        # There should only be exactly one record that meets the criteria
        # at any given time.
        return Response(valid_access)

    def get_access_token(self):
        """ Checks for or creates a Finch Sandbox API access token. 
        """
        # Check in cache
        access_data = cache.get(f'access_data_{self.provider_id}', '')
        if not access_data:
            # Check in db
            database_response = self.get_from_database()
            if not database_response:
                # Call API
                access_payload = {
                    'provider_id': self.provider_id,
                    'products': self.product_scopes
                }
                access_response = requests.post(
                    self.url, json=access_payload, timeout=5)

                if access_response.status_code == 200:
                    access_json = access_response.json()
                    self.add_new_database_record(access_json)

                    cache.set(f'access_data_{self.provider_id}', access_json)
                    print('DEBUG: From API ->', access_json)
                    return access_json
                return Response(status=status.HTTP_400_BAD_REQUEST)
            print('DEBUG: From DB ->', database_response)
            return database_response
        print('DEBUG: From cache ->', access_data)
        return access_data
