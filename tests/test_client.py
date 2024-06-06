import pytest

from rss3_dsl_client.client import Client


@pytest.fixture
def client():
    return Client(base_url="https://gi.rss3.io")


def test_get_activity_by_id(client):
    activity = client.get_activity_by_id("0x000000000000000000000000113f4b4c3765e5f05fd197c5c35b8a8a9b34245b")
    assert "data" in activity
    assert "id" in activity["data"]
    assert activity["data"]["id"] == "0x000000000000000000000000113f4b4c3765e5f05fd197c5c35b8a8a9b34245b"


def test_get_account_activities(client):
    activities = client.get_account_activities("0xd8da6bf26964af9d7eed9e03e53415d37aa96045")
    assert "data" in activities
    assert isinstance(activities["data"], list)


def test_get_rss_activity_by_path(client):
    activity = client.get_rss_activity_by_path("abc")
    assert "data" in activity
    assert isinstance(activity["data"], list)
    assert activity["data"][0]["network"] == "rss"


def test_get_account_activities_with_network(client):
    activities = client.get_account_activities(
        account="vitalik.eth",
        network=["ethereum", "polygon"]
    )
    assert "data" in activities
    assert isinstance(activities["data"], list)
    if activities["data"]:
        for activity in activities["data"]:
            assert "network" in activity


def test_get_account_activities_with_platform(client):
    activities = client.get_account_activities(
        account="vitalik.eth",
        platform=["OpenSea", "Uniswap"]
    )
    assert "data" in activities
    assert isinstance(activities["data"], list)
    if activities["data"]:
        for activity in activities["data"]:
            assert "platform" in activity


def test_get_account_activities_with_tag(client):
    activities = client.get_account_activities(
        account="vitalik.eth",
        tag=["collectible", "exchange"]
    )
    assert "data" in activities
    assert isinstance(activities["data"], list)
    if activities["data"]:
        for activity in activities["data"]:
            assert "tag" in activity


def test_get_account_activities_with_all_filters(client):
    activities = client.get_account_activities(
        account="vitalik.eth",
        network=["farcaster"],
        platform=["Farcaster"],
        tag=["social"],
        limit=50,
        action_limit=5
    )
    assert "data" in activities
    assert isinstance(activities["data"], list)
    if activities["data"]:
        for activity in activities["data"]:
            assert "network" in activity
            assert "platform" in activity
            assert "tag" in activity
