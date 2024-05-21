from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Date, Time
from sqlalchemy.orm import relationship
from .database import Base  # относительный импорт

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    director = Column(String)
    duration = Column(Integer)
    release_year = Column(Integer)  # год выпуска
    rating = Column(Float)  # рейтинг
    genre = Column(String)  # жанр
    seats_available = Column(Integer)  # количество мест

    sessions = relationship("Session", back_populates="movie")

class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    date = Column(Date)  # дата начала
    start_time = Column(Time)  # время начала
    end_time = Column(Time)  # время окончания (по желанию)

    movie = relationship("Movie", back_populates="sessions")
