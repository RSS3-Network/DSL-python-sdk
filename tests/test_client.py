import pytest

from rss3_dsl_client.client import RSS3Client


@pytest.fixture
def client():
    return RSS3Client(base_url="https://gi.rss3.io")


def test_get_account_activities_with_network(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_transaction_transfer_activities(account)
    print(activities)
