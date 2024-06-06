import pytest
from rss3_dsl_client.client import Client


@pytest.fixture
def client():
    return Client(base_url="https://gi.rss3.io")


def test_get_activity_by_id(client):
    activity = client.get_activity_by_id("0x000000000000000000000000113f4b4c3765e5f05fd197c5c35b8a8a9b34245b")
    assert "data" in activity


def test_get_account_activities(client):
    activities = client.get_account_activities("0xd8da6bf26964af9d7eed9e03e53415d37aa96045")
    assert "data" in activities


def test_get_rss_activity_by_path(client):
    activity = client.get_rss_activity_by_path("abc")
    assert "data" in activity
