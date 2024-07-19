# RSS3Client 📡

A client for interacting with the RSS3 Decentralized Service Layer (DSL) API.

## Features ✨

- Fetch various types of activities for an account including collectibles, exchanges, metaverse, social, and transactions.
- Supports pagination and filtering for activity retrieval.
- Retrieve RSS activity details by path.

## Installation 🚀

You can install the required dependencies using pip:

```bash
pip install rss3-dsl-client
```

## Usage 📘

### Initialize the Client

```python
from rss3_dsl_client import RSS3Client

client = RSS3Client()
```

### Fetch Social Post Activities

Here are some examples of fetching social post activities with different parameters:

```python
from rss3_dsl_client.schemas.common import PaginationOptions, ActivityFilter
from rss3_dsl_client.schemas.enums import Platform

# Example 1: Basic usage with pagination
social_post_activities = client.fetch_social_post_activities(
    account="0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
    pagination=PaginationOptions(limit=10)
)
print(social_post_activities)

# Example 2: Using filters for platform
social_post_activities = client.fetch_social_post_activities(
    account="0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
    filters=ActivityFilter(platform=[Platform.FARCASTER, Platform.LENS]),
    pagination=PaginationOptions(limit=10)
)
print(social_post_activities)

# Example 3: Using filters with time range
social_post_activities = client.fetch_social_post_activities(
    account="0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
    filters=ActivityFilter(since_timestamp=1625097600, until_timestamp=1627689600),
    pagination=PaginationOptions(limit=10)
)
print(social_post_activities)
```

### Fetch RSS Activity by Path

You can also fetch RSS activity details by path using the `fetch_rss_activity_by_path` method:

```python
rss_activity = client.fetch_rss_activity_by_path(path="abc")
print(rss_activity)
```

### Other Available Methods

The `RSS3Client` class provides various methods to fetch different types of activities. Below are the available methods:

- `fetch_collectible_approval_activities`
- `fetch_collectible_burn_activities`
- `fetch_collectible_mint_activities`
- `fetch_collectible_trade_activities`
- `fetch_collectible_transfer_activities`
- `fetch_exchange_liquidity_activities`
- `fetch_exchange_staking_activities`
- `fetch_exchange_swap_activities`
- `fetch_metaverse_burn_activities`
- `fetch_metaverse_mint_activities`
- `fetch_metaverse_trade_activities`
- `fetch_metaverse_transfer_activities`
- `fetch_social_comment_activities`
- `fetch_social_delete_activities`
- `fetch_social_mint_activities`
- `fetch_social_profile_activities`
- `fetch_social_proxy_activities`
- `fetch_social_revise_activities`
- `fetch_social_reward_activities`
- `fetch_social_share_activities`
- `fetch_transaction_approval_activities`
- `fetch_transaction_bridge_activities`
- `fetch_transaction_burn_activities`
- `fetch_transaction_mint_activities`
- `fetch_transaction_transfer_activities`

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
