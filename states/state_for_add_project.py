from aiogram.dispatcher.filters.state import State, StatesGroup

class Project(StatesGroup):
    categ = State()
    media = State()
    text = State()


class Done(StatesGroup):
    bir = State()
    ikki = State()
    uch = State()

    
class Shikoyat(StatesGroup):
    bir = State()
    ikki = State()
    uch = State()

class Ochered(StatesGroup):
    bir = State()
    ikki = State()
    uch = State()

