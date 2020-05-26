# -*- coding: utf-8 -*-

"""
    pepipost

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pepipost.api_helper import APIHelper
from pepipost.configuration import Configuration
from pepipost.controllers.base_controller import BaseController
from pepipost.http.auth.custom_header_auth import CustomHeaderAuth
from pepipost.exceptions.api_exception import APIException

class EventsController(BaseController):

    """A Controller to access Endpoints in the pepipost API."""


    def get_events_get(self,
                       startdate,
                       events=None,
                       sort=None,
                       enddate=None,
                       offset=0,
                       limit=10,
                       subject=None,
                       xapiheader=None,
                       fromaddress=None,
                       email=None):
        """Does a GET request to /events.

        Lets you to retrieve the email transaction logs.

        Args:
            startdate (date): The starting date of the statistics to retrieve.
                Must follow format YYYY-MM-DD.
            events (EventsEnum, optional): Filter based on different email
                events. If not passed, all events will be fetched. Multiple
                comma separated events are allowed
            sort (SortEnum, optional): Sort based on email sent time
            enddate (date, optional): The end date of the statistics to
                retrieve. Defaults to today. Must follow format YYYY-MM-DD
            offset (int, optional): The point in the list to begin retrieving
                results.
            limit (int, optional): The number of results to return.
            subject (string, optional): Filter logs based on subject
            xapiheader (string, optional): Filter logs based on recipient's
                email
            fromaddress (string, optional): Filter logs based on fromaddress
            email (string, optional): Filter logs based on recipient's email

        Returns:
            object: Response from the API. API Response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/events'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'startdate': startdate,
            'events': events,
            'sort': sort,
            'enddate': enddate,
            'offset': offset,
            'limit': limit,
            'subject': subject,
            'xapiheader': xapiheader,
            'fromaddress': fromaddress,
            'email': email
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('API Response', _context)
        elif _context.response.status_code == 401:
            raise APIException('API Response', _context)
        elif _context.response.status_code == 403:
            raise APIException('API Response', _context)
        elif _context.response.status_code == 405:
            raise APIException('Invalid input', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body