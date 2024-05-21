from pydantic import BaseModel
from datetime import datetime, date, time

class MovieBase(BaseModel):
    title: str
    description: str
    director: str
    duration: int
    release_year: int  # год выпуска
    rating: float  # рейтинг
    genre: str  # жанр
    seats_available: int  # количество мест

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode: True

class SessionBase(BaseModel):
    movie_id: int
    date: date  # дата начала
    start_time: time  # время начала
    end_time: time = None  # время окончания (по желанию)

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: int
    movie: Movie

    class Config:
        orm_mode: True
