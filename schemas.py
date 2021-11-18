import datetime as _dt
import pydantic as _pydantic


class _BaseJoke(_pydantic.BaseModel):
    setup: str
    punchline: str
    joke: str



class Joke(_BaseJoke):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateJokes(_BaseJoke):
    pass