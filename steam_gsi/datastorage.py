from typing import Union, Dict, Type

from games import Base

_game_states = {}

_fetching_token = None


def update_game_state(
        payload: Union[str, Dict], token: str, state_type: Type[Base]
) -> Base:
    """
    Update stored Game State for token

    :param payload: String or Dict of game data
    :param token: token used in authentication
    :param state_type: Which type of Game State is used
    :return:
    """
    _game_states[token] = state_type.from_json(payload)
    return _game_states[token]


def get_game_state(token: str = None) -> Union[Base, None]:
    """
    Get current Game State for token or set default token

    :param token: token used in authentication
    :return: Stored Game State
    """
    if token:
        return _game_states[token]
    elif _fetching_token:
        return _game_states[_fetching_token]
    else:
        return None


def set_token(token: str = None):
    """
    Set default token
    :param token: token used in authentication
    :return:
    """
    _fetching_token = token

