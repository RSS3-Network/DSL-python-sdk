from datetime import datetime

from rss3_dsl_sdk.schemas.base import Activities, BaseModel, Optional, List, Author


class RssFeedMetadata(BaseModel):
    title: str
    description: str
    pub_date: Optional[datetime] = None
    tags: Optional[List[str]] = None
    authors: Optional[List[Author]] = None


RssFeedActivities = Activities[RssFeedMetadata]
