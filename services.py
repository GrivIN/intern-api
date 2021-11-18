from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas
if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_joke(
    jokes: _schemas.CreateJokes, db: "Session"
) -> _schemas.Joke:
    jokes = _models.Joke(**jokes.dict())
    db.add(jokes)
    db.commit()
    db.refresh(jokes)
    return _schemas.Joke.from_orm(jokes)


async def get_all_jokes(db: "Session") -> List[_schemas.Joke]:
    jokes = db.query(_models.Joke).all()
    return list(map(_schemas.Joke.from_orm, jokes))


async def get_joke(joke_id: int, db: "Session"):
    jokes = db.query(_models.Joke).filter(_models.joke.id == joke_id).first()
    return jokes


async def delete_joke(joke: _models.Joke, db: "Session"):
    db.delete(joke)
    db.commit()


async def update_joke(
    joke_data: _schemas.CreateJokes, joke: _models.Joke, db: "Session"
) -> _schemas.Joke:
    joke.setup = joke_data.setup
    joke.punchline = joke_data.punchline


    db.commit()
    db.refresh(joke)

    return _schemas.Joke.from_orm(joke)