from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from core.database.Base import Base


class PhysicsLab1WorkDB(Base):
    __tablename__ = 'physics_lab_1_work'

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(ForeignKey("users.user_id"), nullable=True)
    work_list = Column(ForeignKey("physics_lab_1_work_list.id"), nullable=True)
    date_time = Column(DateTime)

    user_rel = relationship("UserDB", back_populates="user_physics_work_user")
    work = relationship("PhysicsLab1WorkListDB", back_populates="work")

    def __repr__(self):
        return f"\n<PhysicsLab1WorkDB {self.user_rel.first_name} , {self.work.work_name}>"
