from singer_sdk import typing as th

float_and_string = th.ObjectType(
  th.Property("float", th.NumberType),
  th.Property("opens_count", th.StringType)
)

stats_schema = th.ObjectType(
  th.Property("sent", th.IntegerType),
  th.Property("opens_count", th.IntegerType),
  th.Property("unique_opens_count", th.IntegerType),
  th.Property("clicks_count", th.IntegerType),
  th.Property("unique_clicks_count", th.IntegerType),
  th.Property("unsubscribes_count", th.IntegerType),
  th.Property("spam_count", th.IntegerType),
  th.Property("hard_bounces_count", th.IntegerType),
  th.Property("soft_bounces_count", th.IntegerType),
  th.Property("forwards_count", th.IntegerType),
  th.Property("send_after", th.StringType),
  th.Property("track_opens", th.BooleanType),
  th.Property("open_rate", float_and_string),
  th.Property("click_rate", float_and_string),
  th.Property("unsubscribe_rate", float_and_string),
  th.Property("spam_rate", float_and_string),
  th.Property("hard_bounce_rate", float_and_string),
  th.Property("soft_bounce_rate", float_and_string),
)

email_schema = th.ObjectType(
  th.Property("id", th.StringType),
  th.Property("account_id", th.StringType),
  th.Property("emailable_id", th.StringType),
  th.Property("emailable_type", th.StringType),
  th.Property("emailable_type", th.StringType),
  th.Property("type", th.StringType),
  th.Property("from", th.StringType),
  th.Property("from_name", th.StringType),
  th.Property("name", th.StringType),
  th.Property("subject", th.StringType),
  th.Property("plain_text", th.StringType),
  th.Property("screenshot_url", th.URIType),
  th.Property("preview_url", th.URIType),
  th.Property("created_at", th.DateTimeType),
  th.Property("updated_at", th.DateTimeType),
  th.Property("is_designed", th.BooleanType),
  th.Property("language_id", th.StringType),
  th.Property("is_winner", th.BooleanType),
  th.Property("stats", stats_schema)
)
