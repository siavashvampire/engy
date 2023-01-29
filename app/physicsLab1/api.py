from telegram import User
from app.physicsLab1.model.physics_user_model import PhysicsLab1UserDB
from app.physicsLab1.model.class_model import PhysicsLab1ClassDB
from app.physicsLab1.model.workDB import PhysicsLab1WorkDB
from app.physicsLab1.model.workList import PhysicsLab1WorkListDB
from app.user.model.user_model import UserDB
from core.database.database import session


def get_user(id_in: int = 0, username: str = "", user: User = None, user_id: int = 0) -> PhysicsLab1UserDB:
    id_check = 0
    if id_in != 0:
        id_check = id_in
    if user is not None:
        id_check = user.id

    temp = session.query(PhysicsLab1UserDB).join(UserDB).filter(UserDB.id == id_check).first()
    if temp is not None:
        return temp

    if user_id != 0:
        temp = session.query(PhysicsLab1UserDB).filter(PhysicsLab1UserDB.user_id == user_id).first()
        if temp is not None:
            return temp

    return PhysicsLab1UserDB(user_id=id_check)


def get_class() -> list[PhysicsLab1ClassDB]:
    return session.query(PhysicsLab1ClassDB).all()


def get_work_list_all() -> list[PhysicsLab1WorkListDB]:
    return session.query(PhysicsLab1WorkListDB).order_by(PhysicsLab1WorkListDB.id).all()


def get_work_list_can_insert() -> list[PhysicsLab1WorkListDB]:
    return session.query(PhysicsLab1WorkListDB).filter(PhysicsLab1WorkListDB.can_insert == 1).order_by(
        PhysicsLab1WorkListDB.id).all()


def get_work_list_can_not_insert() -> list[PhysicsLab1WorkListDB]:
    return session.query(PhysicsLab1WorkListDB).filter(PhysicsLab1WorkListDB.can_insert == 0).order_by(
        PhysicsLab1WorkListDB.id).all()


def get_work_by_user_id(user_id: int) -> list[PhysicsLab1WorkDB]:
    return session.query(PhysicsLab1WorkDB).order_by(PhysicsLab1WorkDB.work_list).filter(
        PhysicsLab1WorkDB.user_id == user_id).all()


def get_work_all() -> list[PhysicsLab1WorkDB]:
    return session.query(PhysicsLab1WorkDB).order_by(PhysicsLab1WorkDB.work_list).all()


def get_work_list_by_id(id_in: int) -> PhysicsLab1WorkListDB:
    return session.query(PhysicsLab1WorkListDB).filter(PhysicsLab1WorkListDB.id == id_in).first()


def get_work_by_user_id_work_id(id_in: int, work_id: int) -> PhysicsLab1WorkDB:
    return session.query(PhysicsLab1WorkDB).filter(
        PhysicsLab1WorkDB.user_id == id_in, PhysicsLab1WorkDB.work_list == work_id).first()


def get_work_by_id(id_in: int) -> PhysicsLab1WorkDB:
    return session.query(PhysicsLab1WorkDB).filter(PhysicsLab1WorkDB.id == id_in).first()


def add_user(user_in: User) -> bool:
    return get_user(user=user_in).insert_user()


def check_exist_user(user_in: User) -> bool:
    return get_user(user=user_in).check_exist_user()


def set_user_access(id_in: int, cond: str) -> None:
    if cond == 'accept':
        cond = True
    else:
        cond = False
    get_user(id_in).change_accept(cond)


def get_all_user() -> list[PhysicsLab1UserDB]:
    return session.query(PhysicsLab1UserDB).all()
