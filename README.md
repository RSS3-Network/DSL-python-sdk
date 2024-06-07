# rss3-dsl-client

A Python SDK for interacting with the RSS3 Data Sub Layer (DSL) API.

## Installation

To install `rss3-dsl-client`, you can run the following command:

```sh
pip install rss3-dsl-client
```

## Usage

Here's a simple example of how to use the `rss3-dsl-client` to interact with the RSS3 DSL API.

### Initialize the Client

First, you need to initialize the client with the base URL of the API. You can use different URLs for development and production environments.

#### Production Environment

```python
from rss3_dsl_client.client import Client

# Initialize the client with the production base URL of the API
client = Client(base_url="https://gi.rss3.io")
```

#### Development Environment

```python
from rss3_dsl_client.client import Client

# Initialize the client with the development base URL of the API
client = Client(base_url="https://gi.rss3.dev")
```

### Get Activity Details by Transaction ID

You can retrieve activity details by providing a transaction ID.

```python
# Get activity details by transaction ID
activity = client.get_activity_by_id("0x000000000000000000000000113f4b4c3765e5f05fd197c5c35b8a8a9b34245b")
print(activity)
```

### Get Account Activities

Retrieve a list of activities for a specific account. You can also specify various parameters to filter the results.

```python
# Get account activities with minimal parameters
activities = client.get_account_activities(
    account="0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
    limit=10
)
print(activities)
```

### Get Account Activities with Filters

You can also retrieve activities for a specific account with additional filters.

```python
# Get account activities with network filter
activities = client.get_account_activities(
    account="vitalik.eth",
    network=["ethereum", "polygon"]
)
print(activities)

# Get account activities with platform filter
activities = client.get_account_activities(
    account="vitalik.eth",
    platform=["OpenSea", "Uniswap"]
)
print(activities)

# Get account activities with tag filter
activities = client.get_account_activities(
    account="vitalik.eth",
    tag=["collectible", "exchange"]
)
print(activities)

# Get account activities with multiple filters
activities = client.get_account_activities(
    account="vitalik.eth",
    network=["farcaster"],
    platform=["Farcaster"],
    tag=["social"],
    limit=50,
    action_limit=5
)
print(activities)
```

### Get RSS Activity by Path

Retrieve RSS activity details by providing a specific path.

```python
# Get RSS activity by path
rss_activity = client.get_rss_activity_by_path("abc")
print(rss_activity)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
