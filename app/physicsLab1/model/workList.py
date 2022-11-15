from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database.Base import Base

class PhysicsLab1WorkListDB(Base):
    __tablename__ = 'physics_lab_1_work_list'

    id = Column(Integer, primary_key=True, unique=True)
    work_name = Column(String(50), default="", unique=True)

    work = relationship("PhysicsLab1WorkDB", back_populates="work")
