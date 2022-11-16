from telegram import User
from app.user.model.user_model import UserDB
from core.database.database import session


def get_user(id_in: int = 0, user_id: int = 0, username: str = "", user: User = None) -> UserDB:
    # return UserDB(id=user.id, username=user.username, first_name=user.first_name,
    #               last_name=user.last_name)

    id_check = 0
    if id_in != 0:
        id_check = id_in
    if user is not None:
        id_check = user.id

    if id_check != 0:
        temp = session.query(UserDB).filter(UserDB.id == id_check).first()
        if temp is not None:
            return temp
    if user_id != 0:
        temp = session.query(UserDB).filter(UserDB.user_id == user_id).first()
        if temp is not None:
            return temp

    return UserDB(id=user.id, username=user.username, first_name=user.first_name,
                  last_name=user.last_name)
    # query_text = ""
    # if id_in != 0:
    #     query_text = query.id == id_in
    # elif username != "":
    #     query_text = query.username == username
    # elif user is not None:
    #     return UserDB(telegram_id=user.id, telegram_username=user.username, first_name=user.first_name,
    #                   last_name=user.last_name)
    #
    # search = table.search(query_text)
    #
    # if len(search):
    #     search = search[0]
    #     return UserDB(telegram_id=search['id'])
    # else:
    #     return UserDB()


def add_user(user_in: User):
    return get_user(user=user_in).insert_user()


def get_all_user() -> list[UserDB]:
    users_row = table.all()
    users = []
    for i in users_row:
        users.append(UserDB(id=i['id'], telegram_username=i['username'], first_name=i['first_name'],
                            idea_flag=i["idea_flag"]))
    return users


def check_exist_user(user_in: User) -> bool:
    return get_user(user=user_in).check_exist_user()
