from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from core.database.Base import Base
from core.database.database import session


class PhysicsLab1WorkDB(Base):
    __tablename__ = 'physics_lab_1_work'

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(ForeignKey("users.user_id"), nullable=True)
    work_list = Column(ForeignKey("physics_lab_1_work_list.id"), nullable=True)
    date_time = Column(DateTime)
    score = Column(Integer, nullable=True)

    work = relationship("PhysicsLab1WorkListDB", back_populates="work")
    user_rel = relationship("UserDB", back_populates="user_physics_work_user")

    def update_score(self, score: int) -> None:
        session.query(PhysicsLab1WorkDB).filter(
            PhysicsLab1WorkDB.user_id == self.user_id, PhysicsLab1WorkDB.work_list == self.work_list).update(
            {'score': score})
        session.commit()

    def __repr__(self):
        return f"\n<PhysicsLab1WorkDB {self.user_rel.first_name} , {self.work.work_name}>"
