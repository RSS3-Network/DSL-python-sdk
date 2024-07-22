from rss3_dsl_sdk.schemas.base import Token, Activities


class MetaverseBurnMetadata(Token):
    pass


class MetaverseMintMetadata(Token):
    pass


class MetaverseTradeMetadata(Token):
    pass


class MetaverseTransferMetadata(Token):
    pass


MetaverseBurnActivities = Activities[MetaverseBurnMetadata]
MetaverseMintActivities = Activities[MetaverseMintMetadata]
MetaverseTradeActivities = Activities[MetaverseTradeMetadata]
MetaverseTransferActivities = Activities[MetaverseTransferMetadata]
