from typing import Any, Dict, List, Optional, Literal

import requests

# Enumerations for certain fields to improve usability and type safety
Direction = Literal['in', 'out', 'self']
Network = Literal[
    'arbitrum', 'arweave', 'avax', 'base', 'binance-smart-chain', 'crossbell',
    'ethereum', 'farcaster', 'gnosis', 'linea', 'optimism', 'polygon', 'vsl'
]
Platform = Literal[
    '1inch', 'AAVE', 'Aavegotchi', 'Crossbell', 'Curve', 'ENS', 'Farcaster', 'Highlight',
    'IQWiki', 'KiwiStand', 'Lens', 'Lido', 'LooksRare', 'Matters', 'Mirror', 'OpenSea',
    'Optimism', 'Paragraph', 'RSS3', 'SAVM', 'Stargate', 'Uniswap', 'Unknown', 'VSL'
]
Tag = Literal[
    'collectible', 'exchange', 'metaverse', 'rss', 'social', 'transaction', 'unknown'
]
ActivityType = Literal[
    'approval', 'bridge', 'burn', 'comment', 'delete', 'feed', 'liquidity', 'mint',
    'post', 'profile', 'proxy', 'revise', 'reward', 'share', 'staking', 'swap',
    'trade', 'transfer', 'unknown'
]


class Client:
    """
    A client for interacting with the RSS3 Decentralized Service Layer (DSL) API.
    """

    def __init__(self, base_url: str):
        """
        Initialize the client with the base URL of the RSS3 DSL API.

        :param base_url: The base URL of the API.
        """
        self.base_url = base_url

    def get_activity_by_id(self, id: str, action_limit: int = 10, action_page: int = 1) -> Dict[str, Any]:
        """
        Retrieve activity details by transaction ID.

        :param id: The transaction ID.
        :param action_limit: The limit on the number of actions to retrieve. Default is 10.
        :param action_page: The page number of actions to retrieve. Default is 1.
        :return: A dictionary containing the activity details.
        """
        url = f"{self.base_url}/decentralized/tx/{id}"
        params = {
            "action_limit": action_limit,
            "action_page": action_page
        }
        response = requests.get(url, params=params)
        return response.json()

    def get_account_activities(
            self,
            account: str,
            limit: int = 100,
            action_limit: int = 10,
            cursor: Optional[str] = None,
            since_timestamp: Optional[int] = None,
            until_timestamp: Optional[int] = None,
            success: Optional[bool] = None,
            direction: Optional[Direction] = None,
            network: Optional[List[Network]] = None,
            tag: Optional[List[Tag]] = None,
            type: Optional[List[ActivityType]] = None,
            platform: Optional[List[Platform]] = None
    ) -> Dict[str, Any]:
        """
        Retrieve activities for a specific account.

        :param account: The account address.
        :param limit: The limit on the number of activities to retrieve. Default is 100.
        :param action_limit: The limit on the number of actions to retrieve. Default is 10.
        :param cursor: The cursor for pagination.
        :param since_timestamp: The start timestamp for filtering activities.
        :param until_timestamp: The end timestamp for filtering activities.
        :param success: Filter by success status.
        :param direction: Filter by direction ('in', 'out', 'self').
        :param network: Filter by network (e.g., 'ethereum', 'polygon').
        :param tag: Filter by tags.
        :param type: Filter by types.
        :param platform: Filter by platforms (e.g., 'twitter', 'github').
        :return: A dictionary containing the account activities.
        """
        url = f"{self.base_url}/decentralized/{account}"
        params = {
            "limit": limit,
            "action_limit": action_limit,
            "cursor": cursor,
            "since_timestamp": since_timestamp,
            "until_timestamp": until_timestamp,
            "success": success,
            "direction": direction,
            "network": network,
            "tag": tag,
            "type": type,
            "platform": platform
        }
        response = requests.get(url, params=params)
        return response.json()

    def get_rss_activity_by_path(self, path: str) -> Dict[str, Any]:
        """
        Retrieve RSS activity details by path.

        :param path: The RSS path.
        :return: A dictionary containing the RSS activity details.
        """
        url = f"{self.base_url}/rss/{path}"
        response = requests.get(url)
        return response.json()
