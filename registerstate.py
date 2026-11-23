from aiogram.fsm.state import State , StatesGroup

class Regestrationstate(StatesGroup):
    ism = State()
    familya = State()
    tel_raqam = State()
    tasdiqlash=State()