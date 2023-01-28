from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.user.model.user_model import UserDB
from core.config.database import admin_id
from core.database.Base import Base
from core.database.database import session


class PhysicsLab1UserDB(Base):
    __tablename__ = 'physics_lab_1_users'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(ForeignKey("users.user_id"), primary_key=True, unique=True)
    student_number = Column(Integer, primary_key=True, unique=True, nullable=True)
    class_id = Column(ForeignKey("physics_lab_1_class.id"), nullable=True)
    accept = Column(Boolean, default=0)

    class_rel = relationship("PhysicsLab1ClassDB", back_populates="user_rel")
    user_rel = relationship("UserDB", back_populates="user_physics_user")
    # work_rel = relationship("PhysicsLab1WorkDB", back_populates="user_physics_rel")

    def __init__(self, user_id: int = 0) -> None:

        super().__init__()
        if user_id != 0:
            temp: PhysicsLab1UserDB = session.query(PhysicsLab1UserDB).join(UserDB).filter(
                UserDB.id == user_id).first()

            if temp is not None:
                self.id = temp.id
                self.class_id = temp.class_id
                self.accept = temp.accept
                self.class_rel = temp.class_rel
                self.student_number = temp.student_number
                self.user_rel = temp.user_rel
                self.user_id = temp.user_id

            else:
                temp: UserDB = session.query(UserDB).filter(
                    UserDB.id == user_id).first()
                if temp is not None:
                    self.user_id = temp.user_id
                else:
                    self.user_id = 0

    def insert_user(self) -> bool:
        temp: PhysicsLab1UserDB = session.query(PhysicsLab1UserDB).join(UserDB).filter(
            UserDB.user_id == self.user_id).first()
        if temp is not None:
            return False
        try:
            if not self.student_number:
                self.student_number = self.user_id
            session.add(self)
            session.commit()
            return True
        except:
            return False

    def check_exist_user(self) -> bool:
        temp: PhysicsLab1UserDB = session.query(PhysicsLab1UserDB).join(UserDB).filter(
            UserDB.user_id == self.user_id).first()
        if temp is not None:
            return True
        return False

    def check_access(self) -> bool:
        return self.accept

    def check_admin(self) -> bool:
        return self.user_rel.id == admin_id

    def change_class(self, class_id: int):
        session.query(PhysicsLab1UserDB).filter(PhysicsLab1UserDB.user_id == self.user_id).update(
            {'class_id': class_id})
        self.class_id = class_id
        session.commit()

    def change_accept(self, accept: bool):
        session.query(PhysicsLab1UserDB).filter(PhysicsLab1UserDB.user_id == self.user_id).update(
            {'accept': accept})
        self.accept = accept
        session.commit()

    def change_student_number(self, student_number: int):
        session.query(PhysicsLab1UserDB).filter(PhysicsLab1UserDB.user_id == self.user_id).update(
            {'student_number': student_number})
        self.student_number = student_number
        session.commit()

    def __repr__(self):
        return "<PhysicsUser(%r, %r)>" % (self.user_id, self.id)
