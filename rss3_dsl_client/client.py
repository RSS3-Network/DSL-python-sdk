from typing import Any, Dict, Optional

import requests
from pydantic import validate_call

from rss3_dsl_client.enums import ActivityTag, ActivityType
from rss3_dsl_client.models import PaginationOptions, ActivityFilter, Activities, CollectibleApprovalActivities, \
    CollectibleBurnActivities, CollectibleMintActivities, CollectibleTradeActivities, CollectibleTransferActivities, \
    ExchangeLiquidityMetadata, ExchangeStakingMetadata, ExchangeSwapMetadata, ExchangeLiquidityActivities, \
    ExchangeStakingActivities, ExchangeSwapActivities


class RSS3Client:
    """
    A client for interacting with the RSS3 Decentralized Service Layer (DSL) API.
    """

    def __init__(self, base_url: str):
        """
        Initialize the client with the base URL of the RSS3 DSL API.

        :param base_url: The base URL of the API.
        """
        self.base_url = base_url

    def fetch_activities(
            self,
            account: str,
            tag: Optional[ActivityTag] = None,
            activity_type: Optional[ActivityType] = None,
            pagination: Optional[PaginationOptions] = None,
            filters: Optional[ActivityFilter] = None
    ) -> Activities:
        """
        Retrieve activities for a specific account.

        :param account: The account address.
        :param pagination: Pagination options for the request.
        :param filters: Filters to apply to the activity retrieval.
        :param tag: Tag for the activities.
        :param activity_type: Type for the activities.
        :return: A dictionary containing the account activities.
        """
        response_json = self.__do_fetch_activities(account, tag, activity_type, filters, pagination)
        return Activities(**response_json)

    def __do_fetch_activities(self, account: str,
                              tag: Optional[ActivityTag] = None,
                              activity_type: Optional[ActivityType] = None,
                              pagination: Optional[PaginationOptions] = None,
                              filters: Optional[ActivityFilter] = None) -> dict:
        if pagination is None:
            pagination = PaginationOptions()
        url = f"{self.base_url}/decentralized/{account}"
        params = {
            "limit": pagination.limit,
            "action_limit": pagination.action_limit,
            "cursor": pagination.cursor,
            "since_timestamp": filters.since_timestamp if filters else None,
            "until_timestamp": filters.until_timestamp if filters else None,
            "success": filters.success if filters else None,
            "direction": filters.direction if filters else None,
            "network": filters.network if filters else None,
            "tag": [tag] if tag else None,
            "type": [activity_type] if activity_type else None,
            "platform": filters.platform if filters else None
        }
        response = requests.get(url, params=params)
        response_json = response.json()
        return response_json

    @validate_call
    def fetch_collectible_approval_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> CollectibleApprovalActivities:
        """
        Retrieve collectible approval activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the collectible approval activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.COLLECTIBLE, activity_type=ActivityType.APPROVAL)
        return CollectibleApprovalActivities(**activities)

    @validate_call
    def fetch_collectible_burn_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> CollectibleBurnActivities:
        """
        Retrieve collectible burn activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the collectible burn activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.COLLECTIBLE, activity_type=ActivityType.BURN)
        return CollectibleBurnActivities(**activities)

    @validate_call
    def fetch_collectible_mint_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> CollectibleMintActivities:
        """
        Retrieve collectible mint activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the collectible mint activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.COLLECTIBLE, activity_type=ActivityType.MINT)
        return CollectibleMintActivities(**activities)

    @validate_call
    def fetch_collectible_trade_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> CollectibleTradeActivities:
        """
        Retrieve collectible trade activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the collectible trade activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.COLLECTIBLE, activity_type=ActivityType.TRADE)
        return CollectibleTradeActivities(**activities)

    @validate_call
    def fetch_collectible_transfer_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> CollectibleTransferActivities:
        """
        Retrieve collectible transfer activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the collectible transfer activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.COLLECTIBLE,
                                                activity_type=ActivityType.TRANSFER)
        return CollectibleTransferActivities(**activities)

    @validate_call
    def fetch_exchange_liquidity_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> ExchangeLiquidityActivities:
        """
        Retrieve exchange liquidity activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the exchange liquidity activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.EXCHANGE, activity_type=ActivityType.LIQUIDITY)
        return ExchangeLiquidityActivities(**activities)

    @validate_call
    def fetch_exchange_staking_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> ExchangeStakingActivities:
        """
        Retrieve exchange staking activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the exchange staking activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.EXCHANGE, activity_type=ActivityType.STAKING)
        return ExchangeStakingActivities(**activities)

    @validate_call
    def fetch_exchange_swap_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> ExchangeSwapActivities:
        """
        Retrieve exchange swap activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the exchange swap activities.
        """
        activities = self.__do_fetch_activities(account, pagination=pagination, filters=filters,
                                                tag=ActivityTag.EXCHANGE, activity_type=ActivityType.SWAP)
        return ExchangeSwapActivities(**activities)

    @validate_call
    def fetch_metaverse_burn_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve metaverse burn activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the metaverse burn activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.METAVERSE,
                                     activity_type=ActivityType.BURN)

    @validate_call
    def fetch_metaverse_mint_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve metaverse mint activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the metaverse mint activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.METAVERSE,
                                     activity_type=ActivityType.MINT)

    @validate_call
    def fetch_metaverse_trade_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve metaverse trade activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the metaverse trade activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.METAVERSE,
                                     activity_type=ActivityType.TRADE)

    @validate_call
    def fetch_metaverse_transfer_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve metaverse transfer activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the metaverse transfer activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.METAVERSE,
                                     activity_type=ActivityType.TRANSFER)

    @validate_call
    def fetch_rss_feed_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve RSS feed activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the RSS feed activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.RSS,
                                     activity_type=ActivityType.FEED)

    @validate_call
    def fetch_social_comment_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social comment activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social comment activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.COMMENT)

    @validate_call
    def fetch_social_delete_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social delete activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social delete activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.DELETE)

    @validate_call
    def fetch_social_mint_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social mint activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social mint activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.MINT)

    @validate_call
    def fetch_social_post_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social post activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social post activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.POST)

    @validate_call
    def fetch_social_profile_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social profile activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social profile activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.PROFILE)

    @validate_call
    def fetch_social_proxy_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social proxy activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social proxy activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.PROXY)

    @validate_call
    def fetch_social_revise_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve
        social revise activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social revise activities.
        """

        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.REVISE)

    @validate_call
    def fetch_social_reward_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social reward activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social reward activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.REWARD)

    @validate_call
    def fetch_social_share_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve social share activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the social share activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.SOCIAL,
                                     activity_type=ActivityType.SHARE)

    @validate_call
    def fetch_transaction_approval_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve transaction approval activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the transaction approval activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.TRANSACTION,
                                     activity_type=ActivityType.APPROVAL)

    @validate_call
    def fetch_transaction_bridge_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve transaction bridge activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the transaction bridge activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.TRANSACTION,
                                     activity_type=ActivityType.BRIDGE)

    @validate_call
    def fetch_transaction_burn_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve transaction burn activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the transaction burn activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.TRANSACTION,
                                     activity_type=ActivityType.BURN)

    @validate_call
    def fetch_transaction_mint_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve transaction mint activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the transaction mint activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.TRANSACTION,
                                     activity_type=ActivityType.MINT)

    @validate_call
    def fetch_transaction_transfer_activities(
            self,
            account: str,
            filters: Optional[ActivityFilter] = None,
            pagination: Optional[PaginationOptions] = None
    ) -> Dict[str, Any]:
        """
        Retrieve transaction transfer activities for a specific account.

        :param account: The account address.
        :param filters: Additional filters to apply to the activity retrieval.
        :param pagination: Pagination options for the request.
        :return: A dictionary containing the transaction transfer activities.
        """
        return self.fetch_activities(account, pagination=pagination, filters=filters, tag=ActivityTag.TRANSACTION,
                                     activity_type=ActivityType.TRANSFER)
