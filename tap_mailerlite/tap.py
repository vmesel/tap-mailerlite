"""MailerLite tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_mailerlite.streams.groups import GroupStream
from tap_mailerlite.streams.campaigns import CampaignStream
from tap_mailerlite.streams.subscribers import SubscriberStream


class TapMailerLite(Tap):
    """MailerLite tap class."""

    name = "tap-mailerlite"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.MailerLiteStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            CampaignStream(self),
            SubscriberStream(self),
            GroupStream(self)
        ]


if __name__ == "__main__":
    TapMailerLite.cli()
