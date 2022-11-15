from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database.Base import Base


class PhysicsLab1ClassDB(Base):
    __tablename__ = 'physics_lab_1_class'

    id = Column(Integer, primary_key=True, unique=True)
    class_name = Column(String(50), default="", unique=True)
    class_day = Column(String(50), default="")
    class_time = Column(String(50), default="")

    user_rel = relationship("PhysicsLab1UserDB", back_populates="class_rel")
