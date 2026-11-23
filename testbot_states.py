from aiogram.fsm.state import State, StatesGroup


class oyin_rejimi(StatesGroup):
    sana = State()
    start_game = State()
    game_type = State()
    game_location = State()
    players = State()
    team_name = State()
    enter_game = State()
    after_game = State()
    music_in_game = State()
    izoh = State()