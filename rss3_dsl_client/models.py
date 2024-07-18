from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Union
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from typing import Generic, TypeVar

T = TypeVar('T')

from rss3_dsl_client.enums import Direction, Network, Platform, ActivityTag, ActivityType


class Standard(str, Enum):
    UNKNOWN = 'UNKNOWN'
    ERC20 = 'ERC-20'
    ERC165 = 'ERC-165'
    ERC721 = 'ERC-721'
    ERC1155 = 'ERC-1155'
    ERC1967 = 'ERC-1967'


class Token(BaseModel):
    address: Optional[str] = None
    id: Optional[Decimal] = None
    value: Optional[Decimal] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    uri: Optional[str] = None
    decimals: Optional[int] = None
    standard: Optional[Standard] = None
    parsed_image_url: Optional[str] = None


class NonFungibleTokenMetadata(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image_url: Optional[str]
    external_url: Optional[str]
    media_url: Optional[str]
    animation_url: Optional[str]
    properties: Optional[str]


class ActivityFilter(BaseModel):
    since_timestamp: Optional[int] = None
    until_timestamp: Optional[int] = None
    success: Optional[bool] = None
    direction: Optional[Direction] = None
    network: Optional[List[Network]] = None
    platform: Optional[List[Platform]] = None


class PaginationOptions(BaseModel):
    limit: int = Field(default=10, ge=1)
    action_limit: int = Field(default=10, ge=1)
    cursor: Optional[str] = None


class Fee(BaseModel):
    address: Optional[str] = None
    amount: Decimal
    decimal: int


class Calldata(BaseModel):
    raw: Optional[str] = None
    function_hash: Optional[str] = None
    parsed_function: Optional[str] = None


class CollectibleApprovalMetadata(Token):
    pass


class CollectibleBurnMetadata(Token):
    pass


class CollectibleMintMetadata(Token):
    pass


class CollectibleTradeMetadata(Token):
    pass


class CollectibleTransferMetadata(Token):
    pass


class ExchangeLiquidityMetadata(Token):
    pass


# exchange_staking
class ExchangeStakingMetadata(Token):
    pass


class ExchangeSwapMetadata(BaseModel):
    from_: Token = Field(..., alias="from")
    to: Token


class MetaverseBurnMetadata(Token):
    pass


class MetaverseMintMetadata(Token):
    pass


# fetch_metaverse_trade_activities
class MetaverseTradeMetadata(Token):
    pass


# fetch_metaverse_transfer_activities
class MetaverseTransferMetadata(Token):
    pass


# fetch_social_comment_activities


class Media(BaseModel):
    address: str
    mime_type: str


class SocialPost(BaseModel):
    handle: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    body: Optional[str] = None
    media: Optional[List[Media]] = []
    profile_id: Optional[str] = None
    publication_id: Optional[str] = None
    content_uri: Optional[str] = None
    tags: Optional[List[str]] = []
    author_url: Optional[str] = None
    reward: Optional[Token] = None
    timestamp: Optional[int] = None
    target: Optional['SocialPost'] = None
    target_url: Optional[str] = None


class SocialProfile(BaseModel):
    action: Optional[int] = None
    profile_id: Optional[str] = None
    address: Optional[str] = None
    handle: Optional[str] = None
    image_uri: Optional[str] = None
    bio: Optional[str] = None
    name: Optional[str] = None
    expiry: Optional[datetime] = None
    key: Optional[str] = None
    value: Optional[str] = None

    class Config:
        orm_mode = True


class SocialProxy(BaseModel):
    action: Optional[int] = None
    proxy_address: str
    profile: Optional[SocialProfile] = None


# 	case typex.SocialComment, typex.SocialDelete, typex.SocialMint, typex.SocialPost, typex.SocialRevise, typex.SocialReward, typex.SocialShare:
# 		result = new(SocialPost)
# 	case typex.SocialProfile:
# 		result = new(SocialProfile)
# 	case typex.SocialProxy:
# 		result = new(SocialProxy)
class SocialCommentMetadata(SocialPost):
    pass


class SocialDeleteMetadata(BaseModel):
    pass


class SocialMintMetadata(SocialPost):
    pass


class SocialPostMetadata(SocialPost):
    pass


class SocialReviseMetadata(SocialPost):
    pass


class SocialRewardMetadata(SocialPost):
    pass


class SocialShareMetadata(SocialPost):
    pass


class SocialProfileMetadata(SocialProfile):
    pass


class SocialProxyMetadata(SocialProxy):
    pass


class Action(BaseModel, Generic[T]):
    tag: ActivityTag
    type: ActivityType
    platform: Optional[str] = None
    from_: str = Field(..., alias="from")
    to: str
    metadata: T
    related_urls: Optional[List[str]] = None


class Activity(BaseModel, Generic[T]):
    id: str
    owner: Optional[str] = None
    network: Network
    index: int
    from_: str = Field(..., alias="from")
    to: str
    tag: ActivityTag
    type: ActivityType
    platform: Optional[str] = None
    fee: Optional[Fee] = None
    calldata: Optional[Calldata] = None
    total_actions: int
    actions: List[Action[T]]
    direction: Optional[Direction] = None
    status: bool = Field(..., alias="success")
    timestamp: int


class Meta(BaseModel):
    cursor: Optional[str] = None


class Activities(BaseModel, Generic[T]):
    data: List[Activity[T]]
    meta: Meta


CollectibleApprovalActivities = Activities[CollectibleApprovalMetadata]
CollectibleBurnActivities = Activities[CollectibleBurnMetadata]
CollectibleMintActivities = Activities[CollectibleMintMetadata]
CollectibleTradeActivities = Activities[CollectibleTradeMetadata]
CollectibleTransferActivities = Activities[CollectibleTransferMetadata]

ExchangeLiquidityActivities = Activities[ExchangeLiquidityMetadata]
ExchangeStakingActivities = Activities[ExchangeStakingMetadata]
ExchangeSwapActivities = Activities[ExchangeSwapMetadata]

MetaverseBurnActivities = Activities[MetaverseBurnMetadata]
MetaverseMintActivities = Activities[MetaverseMintMetadata]
MetaverseTradeActivities = Activities[MetaverseTradeMetadata]
MetaverseTransferActivities = Activities[MetaverseTransferMetadata]

SocialCommentActivities = Activities[SocialCommentMetadata]
SocialDeleteActivities = Activities[SocialDeleteMetadata]
SocialMintActivities = Activities[SocialMintMetadata]
SocialPostActivities = Activities[SocialPostMetadata]
SocialReviseActivities = Activities[SocialReviseMetadata]
SocialRewardActivities = Activities[SocialRewardMetadata]
SocialShareActivities = Activities[SocialShareMetadata]
SocialProfileActivities = Activities[SocialProfileMetadata]
SocialProxyActivities = Activities[SocialProxyMetadata]
