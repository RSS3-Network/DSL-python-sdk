from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field

from rss3_dsl_client.enums import Direction, Network, Platform, ActivityTag, ActivityType


class ActivityFilter(BaseModel):
    since_timestamp: Optional[int] = None
    until_timestamp: Optional[int] = None
    success: Optional[bool] = None
    direction: Optional[Direction] = None
    network: Optional[List[Network]] = None
    platform: Optional[List[Platform]] = None


class PaginationOptions(BaseModel):
    limit: int = Field(default=100, ge=1)
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


class Action(BaseModel):
    tag: ActivityTag
    type: ActivityType
    platform: Optional[str] = None
    from_: str = Field(..., alias="from")
    to: str
    metadata: dict
    related_urls: Optional[List[str]] = None


class Activity(BaseModel):
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
    actions: List[Action]
    direction: Optional[Direction] = None
    status: bool = Field(..., alias="success")
    timestamp: int


class Meta(BaseModel):
    cursor: Optional[str] = None


class Activities(BaseModel):
    data: List[Activity]
    meta: Meta
