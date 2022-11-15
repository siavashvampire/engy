from telegram import User
from app.physicsLab1.model.physics_user_model import PhysicsLab1UserDB
from app.physicsLab1.model.class_model import PhysicsLab1ClassDB
from app.user.model.user_model import UserDB
from core.database.database import session


def get_user(id_in: int = 0, username: str = "", user: User = None) -> PhysicsLab1UserDB:
    id_check = 0
    if id_in != 0:
        id_check = id_in
    if user is not None:
        id_check = user.id

    temp = session.query(PhysicsLab1UserDB).join(UserDB).filter(UserDB.id == id_check).first()
    if temp is not None:
        return temp

    return PhysicsLab1UserDB(user_id=id_check)


def get_class() -> list[PhysicsLab1ClassDB]:
    return session.query(PhysicsLab1ClassDB).all()


def add_user(user_in: User) -> bool:
    return get_user(user=user_in).insert_user()


def check_exist_user(user_in: User) -> bool:
    return get_user(user=user_in).check_exist_user()


def set_user_access(id_in, cond):
    if cond == 'accept':
        cond = True
    else:
        cond = False
    get_user(id_in).change_accept(cond)


def get_all_user() -> list[PhysicsLab1UserDB]:
    users_row = table.all()
    users = []
    for i in users_row:
        users.append(PhysicsLab1UserDB(user_id=i['id'], telegram_username=i['username'], first_name=i['first_name'],
                                       idea_flag=i["idea_flag"]))
    return users
