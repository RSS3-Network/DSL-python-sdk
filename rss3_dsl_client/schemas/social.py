from datetime import datetime

from rss3_dsl_client.schemas.common import Token, Activities, BaseModel, Media, Optional, List


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


class SocialProxy(BaseModel):
    action: Optional[int] = None
    proxy_address: str
    profile: Optional[SocialProfile] = None


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


SocialCommentActivities = Activities[SocialCommentMetadata]
SocialDeleteActivities = Activities[SocialDeleteMetadata]
SocialMintActivities = Activities[SocialMintMetadata]
SocialPostActivities = Activities[SocialPostMetadata]
SocialReviseActivities = Activities[SocialReviseMetadata]
SocialRewardActivities = Activities[SocialRewardMetadata]
SocialShareActivities = Activities[SocialShareMetadata]
SocialProfileActivities = Activities[SocialProfileMetadata]
SocialProxyActivities = Activities[SocialProxyMetadata]
