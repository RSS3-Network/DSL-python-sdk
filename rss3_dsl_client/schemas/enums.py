from enum import Enum


class Direction(str, Enum):
    IN = 'in'
    OUT = 'out'
    SELF = 'self'


class Network(str, Enum):
    ARBITRUM = 'arbitrum'
    ARWEAVE = 'arweave'
    AVAX = 'avax'
    BASE = 'base'
    BINANCE_SMART_CHAIN = 'binance-smart-chain'
    CROSSBELL = 'crossbell'
    ETHEREUM = 'ethereum'
    FARCASTER = 'farcaster'
    GNOSIS = 'gnosis'
    LINEA = 'linea'
    OPTIMISM = 'optimism'
    POLYGON = 'polygon'
    VSL = 'vsl'
    RSS = 'rss'


class Platform(str, Enum):
    INCH = '1inch'
    AAVE = 'AAVE'
    AAVEGOTCHI = 'Aavegotchi'
    CROSSBELL = 'Crossbell'
    CURVE = 'Curve'
    ENS = 'ENS'
    FARCASTER = 'Farcaster'
    HIGHLIGHT = 'Highlight'
    IQWIKI = 'IQWiki'
    KIWISTAND = 'KiwiStand'
    LENS = 'Lens'
    LIDO = 'Lido'
    LOOKSRARE = 'LooksRare'
    MATTERS = 'Matters'
    MIRROR = 'Mirror'
    OPENSEA = 'OpenSea'
    OPTIMISM = 'Optimism'
    PARAGRAPH = 'Paragraph'
    RSS3 = 'RSS3'
    SAVM = 'SAVM'
    STARGATE = 'Stargate'
    UNISWAP = 'Uniswap'
    UNKNOWN = 'Unknown'
    VSL = 'VSL'


class ActivityTag(str, Enum):
    COLLECTIBLE = 'collectible'
    EXCHANGE = 'exchange'
    METAVERSE = 'metaverse'
    RSS = 'rss'
    SOCIAL = 'social'
    TRANSACTION = 'transaction'
    UNKNOWN = 'unknown'


class ActivityType(str, Enum):
    APPROVAL = 'approval'
    BRIDGE = 'bridge'
    BURN = 'burn'
    COMMENT = 'comment'
    DELETE = 'delete'
    FEED = 'feed'
    LIQUIDITY = 'liquidity'
    MINT = 'mint'
    POST = 'post'
    PROFILE = 'profile'
    PROXY = 'proxy'
    REVISE = 'revise'
    REWARD = 'reward'
    SHARE = 'share'
    STAKING = 'staking'
    SWAP = 'swap'
    TRADE = 'trade'
    TRANSFER = 'transfer'
    UNKNOWN = 'unknown'


class Standard(str, Enum):
    UNKNOWN = 'UNKNOWN'
    ERC20 = 'ERC-20'
    ERC165 = 'ERC-165'
    ERC721 = 'ERC-721'
    ERC1155 = 'ERC-1155'
    ERC1967 = 'ERC-1967'
