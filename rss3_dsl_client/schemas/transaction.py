from rss3_dsl_client.schemas.common import Token, Activities, BaseModel, Network


class TransactionBridge(BaseModel):
    action: str
    source_network: Network
    target_network: Network
    token: Token


class TransactionApprovalMetadata(Token):
    pass


class TransactionBridgeMetadata(TransactionBridge):
    pass


class TransactionBurnMetadata(Token):
    pass


class TransactionMintMetadata(Token):
    pass


class TransactionTransferMetadata(Token):
    pass


TransactionApprovalActivities = Activities[TransactionApprovalMetadata]
TransactionBridgeActivities = Activities[TransactionBridgeMetadata]
TransactionBurnActivities = Activities[TransactionBurnMetadata]
TransactionMintActivities = Activities[TransactionMintMetadata]
TransactionTransferActivities = Activities[TransactionTransferMetadata]
