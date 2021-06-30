from . import Base
from enum import Enum
from dataclasses import dataclass, field


class TeamPrefixes(str, Enum):
    RADIANT = "dota_goodguys"
    DIRE = "dota_badguys"


class GameStates(str, Enum):
    IN_PROGRESS = "DOTA_GAMERULES_STATE_GAME_IN_PROGRESS"
    POST_GAME = "DOTA_GAMERULES_STATE_POST_GAME"
    PRE_GAME = "DOTA_GAMERULES_STATE_PRE_GAME"


class PlayerActivity(str, Enum):
    PLAYING = "playing"


@dataclass
class Building(Base):
    name: str
    health: int
    max_health: int


@dataclass
class TeamBuildings(Base):
    top_t1: Building = field(default=None)
    top_t2: Building = field(default=None)
    top_t3: Building = field(default=None)
    top_t4: Building = field(default=None)
    mid_t1: Building = field(default=None)
    mid_t2: Building = field(default=None)
    mid_t3: Building = field(default=None)
    bot_t1: Building = field(default=None)
    bot_t2: Building = field(default=None)
    bot_t3: Building = field(default=None)
    bot_t4: Building = field(default=None)
    top_rax_melee: Building = field(default=None)
    top_rax_ranged: Building = field(default=None)
    mid_rax_melee: Building = field(default=None)
    mid_rax_ranged: Building = field(default=None)
    bot_rax_melee: Building = field(default=None)
    bot_rax_ranged: Building = field(default=None)
    ancient: Building = field(default=None)


@dataclass
class Buildings(Base):
    radiant: TeamBuildings = field(default=None)
    dire: TeamBuildings = field(default=None)


@dataclass
class Hero(Base):
    id: int


@dataclass
class Abilities(Base):
    pass


@dataclass
class Items(Base):
    pass


@dataclass
class Draft(Base):
    pass


@dataclass
class Wearables(Base):
    pass


@dataclass
class Player(Base):
    steam_id: str
    name: str
    activity: PlayerActivity
    kills: int
    deaths: int
    assists: int
    last_hits: int
    denies: int
    kill_streak: int
    commands_issued: int
    team_name: str
    gold: int
    gold_reliable: int
    gold_unreliable: int
    gold_from_hero_kills: int
    gold_from_creep_kills: int
    gold_from_income: int
    gpm: int
    xpm: int


@dataclass
class Map(Base):
    name: str
    match_id: str
    game_time: int
    clock_time: int
    daytime: bool
    nightstalker_night: bool
    game_state: GameStates
    paused: bool
    win_team: str
    custom_game_name: str
    ward_purchase_cooldown: int


@dataclass
class GameState(Base):
    buildings: Buildings = field(default=None)
    map: Map = field(default=None)
    player: Player = field(default=None)
    hero: Hero = field(default=None)
    previously: 'GameState' = field(default=None)
