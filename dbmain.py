from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/jokes/", response_model=_schemas.Joke)
async def create_joke(
    joke: _schemas.CreateJokes,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_Joke(joke=joke, db=db)


@app.get("/api/jokes/", response_model=List[_schemas.Joke])
async def get_joke(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_jokes(db=db)


@app.get("/api/jokes/{joke_id}/", response_model=_schemas.Joke)
async def get_joke(
    joke_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    joke = await _services.get_joke(db=db, joke_id=joke_id)
    if joke is None:
        raise _fastapi.HTTPException(status_code=404, detail="Joke does not exist")

    return joke


@app.delete("/api/jokes/{joke_id}/")
async def delete_joke(
    joke_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    joke = await _services.get_joke(db=db, joke_id=joke_id)
    if joke is None:
        raise _fastapi.HTTPException(status_code=404, detail="Joke does not exist")

    await _services.delete_joke(joke, db=db)

    return "successfully deleted the joke"


@app.put("/api/jokes/{joke_id}/", response_model=_schemas.Joke)
async def update_joke(
    joke_id: int,
    joke_data: _schemas.CreateJokes,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    joke = await _services.get_joke(db=db, joke_id=joke_id)
    if joke is None:
        raise _fastapi.HTTPException(status_code=404, detail="Joke does not exist")

    return await _services.update_joke(
        joke_data=joke_data, joke=joke, db=db
    )