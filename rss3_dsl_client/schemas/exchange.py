from rss3_dsl_client.schemas.common import Token, Activities, BaseModel, Field


class ExchangeLiquidityMetadata(Token):
    pass


class ExchangeStakingMetadata(Token):
    pass


class ExchangeSwapMetadata(BaseModel):
    from_: Token = Field(..., alias="from")
    to: Token


ExchangeLiquidityActivities = Activities[ExchangeLiquidityMetadata]
ExchangeStakingActivities = Activities[ExchangeStakingMetadata]
ExchangeSwapActivities = Activities[ExchangeSwapMetadata]
