from rss3_dsl_client.schemas.common import Token, Activities


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


CollectibleApprovalActivities = Activities[CollectibleApprovalMetadata]
CollectibleBurnActivities = Activities[CollectibleBurnMetadata]
CollectibleMintActivities = Activities[CollectibleMintMetadata]
CollectibleTradeActivities = Activities[CollectibleTradeMetadata]
CollectibleTransferActivities = Activities[CollectibleTransferMetadata]
