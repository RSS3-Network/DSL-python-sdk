# rss3-dsl-client

A Python SDK for interacting with the RSS3 Data Sub Layer (DSL) API.

## Installation

To install `rss3-dsl-client`, you can use [Poetry](https://python-poetry.org/). First, ensure you have Poetry installed, then run:

```sh
poetry add rss3-dsl-client
```

This will add `rss3-dsl-client` to your project's dependencies.

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
# Get account activities
activities = client.get_account_activities(
    account="0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
    limit=50,
    action_limit=5,
    since_timestamp=1609459200,  # January 1, 2021
    until_timestamp=1640995200,  # January 1, 2022
    success=True,
    direction="in",
    network=["ethereum", "polygon"],
    tag=["exchange", "transaction"],
    type=["transfer", "swap"],
    platform=["Uniswap", "OpenSea"]
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
