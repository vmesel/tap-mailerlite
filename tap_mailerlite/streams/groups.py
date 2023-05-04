from singer_sdk import typing as th

from tap_mailerlite.client import MailerLiteStream
from .utils import *

class GroupStream(MailerLiteStream):
    """Define custom stream."""

    name = "group"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.EmailType),
        th.Property("active_count", th.IntegerType),
        th.Property("sent_count", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property(
        "open_rate", float_and_string
        ),
        th.Property("clicks_count", th.NumberType),
        th.Property("click_rate", float_and_string),
        th.Property("created_at", th.DateTimeType),
        th.Property("unsubscribed_count", th.IntegerType),
        th.Property("unconfirmed_count", th.IntegerType),
        th.Property("bounced_count", th.IntegerType),
        th.Property("junk_count", th.IntegerType)
    ).to_dict()