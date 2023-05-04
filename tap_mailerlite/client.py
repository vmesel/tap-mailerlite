from pathlib import Path
from typing import Any, Callable, Iterable

import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseHATEOASPaginator
from singer_sdk.streams import RESTStream

from urllib.parse import parse_qsl

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class MailerLitePaginator(BaseHATEOASPaginator):
    def get_next_url(self, response, previous_token=None):
        data = response.json()
        return data.get("links", {}).get("next", None)

class MailerLiteStream(RESTStream):
    """MailerLite stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://connect.mailerlite.com/api"

    records_jsonpath = "$.data[*]"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("auth_token", ""),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        return headers
    
    def get_new_paginator(self):
        return MailerLitePaginator()

    def get_url_params(self, context, next_page_token):
        params = {}

        if next_page_token:
            params.update(parse_qsl(next_page_token.query))

        return params

    def prepare_request_payload(self, context, next_page_token):
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row, context):
        return row
