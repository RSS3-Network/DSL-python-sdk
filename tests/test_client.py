import pytest

from rss3_dsl_client.client import RSS3Client


@pytest.fixture
def client():
    return RSS3Client(base_url="https://gi.rss3.io")


def test_fetch_transaction_transfer_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_transaction_transfer_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_collectible_approval_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_collectible_approval_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_collectible_burn_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_collectible_burn_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_collectible_mint_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_collectible_mint_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_collectible_trade_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_collectible_trade_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_collectible_transfer_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_collectible_transfer_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_exchange_liquidity_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_exchange_liquidity_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_exchange_staking_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_exchange_staking_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_exchange_swap_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_exchange_swap_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_metaverse_burn_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_metaverse_burn_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_metaverse_mint_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_metaverse_mint_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_metaverse_trade_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_metaverse_trade_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_metaverse_transfer_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_metaverse_transfer_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_comment_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_comment_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_delete_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_delete_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_mint_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_mint_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_post_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_post_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_profile_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_profile_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_proxy_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_proxy_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_revise_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_revise_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_reward_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_reward_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_social_share_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_social_share_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_transaction_approval_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_transaction_approval_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_transaction_bridge_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_transaction_bridge_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_transaction_burn_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_transaction_burn_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_transaction_mint_activities(client):
    account = "0xd8da6bf26964af9d7eed9e03e53415d37aa96045"
    activities = client.fetch_transaction_mint_activities(account)
    assert activities is not None
    assert isinstance(activities.data, list)


def test_fetch_rss_activity_by_path(client):
    path = "abc"
    activities = client.fetch_rss_activity_by_path(path)
    assert activities is not None
    assert isinstance(activities.data, list)
