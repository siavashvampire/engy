from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from core.database.Base import Base

user = 'engy_siavash'
password = 'VamPire1468'
host = '127.0.0.1'
port = 3306
database = 'engy'


def get_connection() -> Engine:
    return create_engine(
        url="mysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


engine = get_connection()

session = sessionmaker(bind=engine)()


def create_db() -> None:
    from app.physicsLab1.model.workList import PhysicsLab1WorkListDB
    from app.physicsLab1.model.workDB import PhysicsLab1WorkDB
    from app.user.model.user_model import UserDB
    from app.physicsLab1.model.class_model import PhysicsLab1ClassDB
    from app.physicsLab1.model.physics_user_model import PhysicsLab1UserDB

    PhysicsLab1WorkListDB()
    PhysicsLab1WorkDB()
    UserDB()
    PhysicsLab1ClassDB()
    PhysicsLab1UserDB()
    Base.metadata.create_all(engine)

    # session.add(ed_user)
