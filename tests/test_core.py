"""Tests standard tap features using the built-in SDK tests library."""

import datetime
import json
from singer_sdk.testing import get_tap_test_class

from tap_mailerlite.tap import TapMailerLite

try:
    loaded_config = json.load(open(".secrets/config.json", "r"))
    auth_token = loaded_config["auth_token"]
except FileNotFoundError:
    auth_token = "invalid_auth_token"

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "auth_token": auth_token
}

TestTapMailerLite = get_tap_test_class(
    tap_class=TapMailerLite,
    config=SAMPLE_CONFIG,
)