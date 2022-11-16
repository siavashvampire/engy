from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.physicsLab1.model.workDB import PhysicsLab1WorkDB
from core.database.Base import Base
from core.database.database import session


class PhysicsLab1WorkListDB(Base):
    __tablename__ = 'physics_lab_1_work_list'

    id = Column(Integer, primary_key=True, unique=True)
    work_name = Column(String(50), default="", unique=True)

    work = relationship("PhysicsLab1WorkDB", back_populates="work")

    def insert_data(self, user_id):
        from app.physicsLab1.api import get_user
        work = PhysicsLab1WorkDB()
        user = get_user(user_id)
        work.user_id = user.user_rel.user_id
        work.work_list = self.id
        work.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            session.add(work)
            session.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def __repr__(self):
        return f"\n<PhysicsLab1WorkListDB  {self.work_name}>"