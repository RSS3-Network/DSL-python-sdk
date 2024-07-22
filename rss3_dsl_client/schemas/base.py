from decimal import Decimal
from typing import Generic, TypeVar, List, Optional

from pydantic import BaseModel, Field

from rss3_dsl_client.schemas.enums import Direction, Network, ActivityTag, ActivityType, Standard, Platform

T = TypeVar('T')


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


class Fee(BaseModel):
    address: Optional[str] = None
    amount: Decimal
    decimal: int


class Calldata(BaseModel):
    raw: Optional[str] = None
    function_hash: Optional[str] = None
    parsed_function: Optional[str] = None


class Media(BaseModel):
    address: str
    mime_type: str


class Author(BaseModel):
    name: str


class PaginationOptions(BaseModel):
    limit: int = Field(default=10, ge=1)
    action_limit: int = Field(default=10, ge=1)
    cursor: Optional[str] = None


class ActivityFilter(BaseModel):
    since_timestamp: Optional[int] = None
    until_timestamp: Optional[int] = None
    success: Optional[bool] = None
    direction: Optional[Direction] = None
    network: Optional[List[Network]] = None
    platform: Optional[List[Platform]] = None


class Meta(BaseModel):
    cursor: Optional[str] = None


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


class Activities(BaseModel, Generic[T]):
    data: List[Activity[T]]
    meta: Optional[Meta] = None
