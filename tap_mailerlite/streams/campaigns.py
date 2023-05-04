from singer_sdk import typing as th

from tap_mailerlite.client import MailerLiteStream
from .utils import *

class CampaignStream(MailerLiteStream):
    """Define custom stream."""

    name = "Campaign"
    path = "/campaigns"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("account_id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("missing_data", th.ArrayType(th.StringType)),
        th.Property(
            "stats", float_and_string
        ),
        th.Property(
            "settings", th.ObjectType(
                th.Property("track_opens", th.StringType),
                th.Property("use_google_analytics", th.StringType),
                th.Property("ecommerce_tracking", th.StringType),
            )
        ),
        th.Property("filter_for_humans", th.ArrayType(th.ArrayType(th.StringType))),
        th.Property("delivery_schedule", th.StringType),
        th.Property("language_id", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("scheduled_for", th.DateTimeType),
        th.Property("queued_at", th.DateTimeType),
        th.Property("started_at", th.DateTimeType),
        th.Property("finished_at", th.DateTimeType),
        th.Property("stopped_at", th.DateTimeType),
        th.Property("default_email_id", th.StringType),
        th.Property("emails", th.ArrayType(email_schema)),
        th.Property("used_in_automations", th.BooleanType),
        th.Property("is_stopped", th.BooleanType),
        th.Property("uses_ecommerce", th.BooleanType),
        th.Property("uses_survey", th.BooleanType),
        th.Property("can_be_scheduled", th.BooleanType),
        th.Property("is_currently_sending_out", th.BooleanType),
        th.Property("type_for_humans", th.StringType),
        th.Property("has_winner", th.StringType),
        th.Property("winner_version_for_human", th.StringType),
        th.Property("winner_sending_time_for_humans", th.StringType),
        th.Property("winner_selected_manually_at", th.DateTimeType),
        th.Property("initial_created_at", th.DateTimeType),
        th.Property("warnings", th.ArrayType(th.StringType)),
    ).to_dict()