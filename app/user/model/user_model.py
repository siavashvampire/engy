from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from telegram import User

from core.database.Base import Base
from core.database.database import session


# from core.config.database import admin_id


class UserDB2(User):
    idea_flag: bool

    def __init__(self, id_in: int = 0, username: str = "", first_name: str = "",
                 last_name: str = "", idea_flag: bool = False, accounting_flag: bool = False):
        self.table = table

        if id_in != 0 and username == "":
            self.id = id_in
            search = self.table.get(query.id == self.id)
            username = search['username']
            first_name = search['first_name']
            self.idea_flag = search['idea_flag']
            self.accounting_flag = search['accounting_flag']
        else:
            self.idea_flag = idea_flag
            self.accounting_flag = accounting_flag

        super().__init__(id=id_in, first_name=first_name, is_bot=False, last_name=last_name, username=username)

    def insert_user(self):
        self.table.upsert(
            {'id': self.id, 'username': self.username, 'first_name': self.first_name,
             'idea_flag': self.idea_flag, 'accounting_flag': self.accounting_flag},
            query.id == self.id)

    def is_idea_admin(self):
        if self.id == idea_admin_id:
            return True
        return False

    def is_accounting_admin(self):
        if self.id == accounting_admin_id:
            return True
        return False

    def can_insert_idea(self):
        return True
        if self.idea_flag:
            return True
        return False

    def can_insert_accounting(self):
        if self.accounting_flag:
            return True
        return False

    def change_idea_flag(self, value: bool):
        self.table.update({'idea_flag': value}, query.id == self.id)

    def change_accounting_flag(self, value: bool):
        self.table.update({'accounting_flag': value}, query.id == self.id)


class UserDB(User, Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))

    user_physics_user = relationship("PhysicsLab1UserDB", back_populates="user_rel")
    user_physics_work_user = relationship("PhysicsLab1WorkDB", back_populates="user_rel")

    def __init__(self, id: int = 0, username: str = "", first_name: str = "",
                 last_name: str = "") -> None:

        temp: UserDB = session.query(UserDB).filter(
            UserDB.id == id).first()
        if temp is not None:
            self.id = temp.id
            self.user_id = temp.user_id
            self.first_name = temp.first_name
            self.last_name = temp.last_name
            self.username = temp.username
            self.user_physics_user = temp.user_physics_user
        else:
            self.id = id
            self.first_name = first_name
            self.last_name = last_name
            self.username = username

        # if id != 0 and username == "":
        # else:
        #     self.id = id
        #     self.user_id = temp.user_id
        #     self.first_name = temp.first_name
        #     self.last_name = temp.last_name
        #     self.username = temp.username
        #     self.user_physics_user = temp.user_physics_user

        User.__init__(self=self, id=id, first_name=first_name, last_name=last_name, is_bot=False,
                      username=username)
        Base.__init__(self)

    def insert_user(self) -> bool:
        temp: UserDB = session.query(UserDB).filter(
            UserDB.id == self.id).first()
        if temp is not None:
            return False
        try:
            session.add(self)
            session.commit()
            return True
        except:
            return False

    def check_exist_user(self) -> bool:
        temp: UserDB = session.query(UserDB).filter(UserDB.id == self.id).first()
        if temp is not None:
            return True
        return False

    def __repr__(self):
        return "<User(%r, %r)>" % (self.first_name, self.id)
