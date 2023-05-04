from singer_sdk import typing as th

from tap_mailerlite.client import MailerLiteStream
from .utils import *

class SubscriberStream(MailerLiteStream):
    """Define custom stream."""

    name = "subscriber"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("email", th.EmailType),
        th.Property("status", th.StringType),
        th.Property("source", th.StringType),
        th.Property("sent", th.IntegerType),
        th.Property("opens_count", th.NumberType),
        th.Property("clicks_count", th.NumberType),
        th.Property("open_rate", th.NumberType),
        th.Property("click_rate", th.NumberType),
        th.Property("ip_address", th.IPv4Type),
        th.Property("optin_ip", th.IPv4Type),
        th.Property("click_rate", th.NumberType),
        th.Property("subscribed_at", th.DateTimeType),
        th.Property("unsubscribed_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("opted_in_at", th.DateTimeType),
        th.Property(
            "fields", th.ObjectType(
                th.Property("city", th.StringType),
                th.Property("company", th.StringType),
                th.Property("country", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("name", th.StringType),
                th.Property("phone", th.StringType),
                th.Property("state", th.StringType),
                th.Property("z_i_p", th.StringType),
            )
        ),
        th.Property("groups", th.ArrayType(th.StringType))
    ).to_dict()