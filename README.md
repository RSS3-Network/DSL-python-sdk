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

```python
from rss3_dsl_client.client import Client

# Initialize the client with the base URL of the API
client = Client(base_url="https://gi.rss3.io")

# Get activity details by transaction ID
activity = client.get_activity_by_id("0x000000000000000000000000113f4b4c3765e5f05fd197c5c35b8a8a9b34245b")
print(activity)

# Get account activities
activities = client.get_account_activities("0xd8da6bf26964af9d7eed9e03e53415d37aa96045")
print(activities)

# Get RSS activity by path
rss_activity = client.get_rss_activity_by_path("abc")
print(rss_activity)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
