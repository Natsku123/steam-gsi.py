from steam_gsi.games import Base
from enum import Enum
from dataclasses import dataclass, field


class TeamPrefixes(str, Enum):
    """
    Prefixes used for the teams
    """
    RADIANT = "dota_goodguys"
    DIRE = "dota_badguys"


class GameStates(str, Enum):
    """
    Overview of Game State
    """
    IN_PROGRESS = "DOTA_GAMERULES_STATE_GAME_IN_PROGRESS"
    POST_GAME = "DOTA_GAMERULES_STATE_POST_GAME"
    PRE_GAME = "DOTA_GAMERULES_STATE_PRE_GAME"


class PlayerActivity(str, Enum):
    """
    Player Activity status
    """
    PLAYING = "playing"


@dataclass
class Building(Base):
    """
    Building on the map
    """
    health: int
    max_health: int


@dataclass
class TeamBuildingsRadiant(Base):
    """
    Buildings for Radiant
    """
    dota_goodguys_tower1_top: Building = field(default=None)
    dota_goodguys_tower2_top: Building = field(default=None)
    dota_goodguys_tower3_top: Building = field(default=None)
    dota_goodguys_tower4_top: Building = field(default=None)
    dota_goodguys_tower1_mid: Building = field(default=None)
    dota_goodguys_tower2_mid: Building = field(default=None)
    dota_goodguys_tower3_mid: Building = field(default=None)
    dota_goodguys_tower1_bot: Building = field(default=None)
    dota_goodguys_tower2_bot: Building = field(default=None)
    dota_goodguys_tower3_bot: Building = field(default=None)
    dota_goodguys_tower4_bot: Building = field(default=None)
    good_rax_melee_top: Building = field(default=None)
    good_rax_ranged_top: Building = field(default=None)
    good_rax_melee_mid: Building = field(default=None)
    good_rax_ranged_mid: Building = field(default=None)
    good_rax_melee_bot: Building = field(default=None)
    good_rax_ranged_bot: Building = field(default=None)
    dota_goodguys_fort: Building = field(default=None)


@dataclass
class TeamBuildingsDire(Base):
    """
    Buildings for Dire
    """
    dota_badguys_tower1_top: Building = field(default=None)
    dota_badguys_tower2_top: Building = field(default=None)
    dota_badguys_tower3_top: Building = field(default=None)
    dota_badguys_tower4_top: Building = field(default=None)
    dota_badguys_tower1_mid: Building = field(default=None)
    dota_badguys_tower2_mid: Building = field(default=None)
    dota_badguys_tower3_mid: Building = field(default=None)
    dota_badguys_tower1_bot: Building = field(default=None)
    dota_badguys_tower2_bot: Building = field(default=None)
    dota_badguys_tower3_bot: Building = field(default=None)
    dota_badguys_tower4_bot: Building = field(default=None)
    bad_rax_melee_top: Building = field(default=None)
    bad_rax_ranged_top: Building = field(default=None)
    bad_rax_melee_mid: Building = field(default=None)
    bad_rax_ranged_mid: Building = field(default=None)
    bad_rax_melee_bot: Building = field(default=None)
    bad_rax_ranged_bot: Building = field(default=None)
    dota_badguys_fort: Building = field(default=None)


@dataclass
class Buildings(Base):
    """
    Buildings Root Object
    """
    radiant: TeamBuildingsRadiant = field(default=None)
    dire: TeamBuildingsDire = field(default=None)


@dataclass
class Hero(Base):
    """
    Hero selected played
    """
    id: int


@dataclass
class Abilities(Base):
    """
    Available abilities
    """
    pass


@dataclass
class Items(Base):
    """
    Available items
    """
    pass


@dataclass
class Draft(Base):
    """
    Drafted heroes
    """
    pass


@dataclass
class Wearables(Base):
    """
    Wearables
    """
    pass


@dataclass
class Player(Base):
    """
    Player-object
    """
    steamid: str
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
    """
    Map / Game data
    """
    name: str
    matchid: str
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
class Auth(Base):
    """
    Auth object
    """
    token: str


@dataclass
class GameState(Base):
    """
    GameState Root Object
    """
    buildings: Buildings = field(default=None)
    map: Map = field(default=None)
    player: Player = field(default=None)
    hero: Hero = field(default=None)
    previously: 'GameState' = field(default=None)
    auth: Auth = field(default=None)
