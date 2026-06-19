from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///./swimtimes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    gender = Column(String, nullable=True)       # "male" or "female"
    team1 = Column(String, nullable=True)
    team2 = Column(String, nullable=True)
    team3 = Column(String, nullable=True)
    times = relationship("SwimTime", back_populates="swimmer")


class SwimTime(Base):
    __tablename__ = "swim_times"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    event = Column(String, nullable=False)   # e.g. "100 Freestyle"
    course = Column(String, nullable=False)  # "SCY" or "LCM"
    time_seconds = Column(Float, nullable=False)
    swimmer = relationship("User", back_populates="times")
    __table_args__ = (UniqueConstraint("user_id", "event", "course", name="uq_user_event_course"),)


def init_db():
    Base.metadata.create_all(bind=engine)
