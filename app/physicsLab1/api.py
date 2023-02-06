from telegram import User
from app.physicsLab1.model.physics_user_model import PhysicsLab1UserDB
from app.physicsLab1.model.class_model import PhysicsLab1ClassDB
from app.physicsLab1.model.workDB import PhysicsLab1WorkDB
from app.physicsLab1.model.workList import PhysicsLab1WorkListDB
from app.user.model.user_model import UserDB
from core.database.database import session

import pandas as pd

import openpyxl
import xlsxwriter


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


def set_score_from_excel():
    df = pd.read_excel('./physicsLab1_all.xlsx')

    update_index = 2

    for _, row in df.iterrows():
        works = row[update_index + 1:]
        user_id = row[0]
        for idx, work in enumerate(works):
            if (type(work) == float or type(work) == int) and not work != work:
                try:
                    work_temp = get_work_by_user_id_work_id(user_id, idx + 1)
                    work_temp.update_score(work)
                except:
                    print(user_id, idx + 1)


def remove(sheet, row):
    for cell in row:
        if cell.value is not None:
            return
    sheet.delete_rows(row[0].row, 1)


def prepare_all_score(path_xlsx: str = './physicsLab1_all.xlsx') -> None:
    workbook = xlsxwriter.Workbook(path_xlsx)

    worksheet = workbook.add_worksheet('scores')
    cell_format = workbook.add_format()

    cell_format.set_align('center')
    cell_format.set_align('vcenter')

    index = 0

    worksheet.write(0, index, 'user_id', cell_format)
    index += 1

    worksheet.write(0, index, 'نام', cell_format)
    index += 1

    worksheet.write(0, index, 'شماره دانشجویی', cell_format)
    index += 1

    works_list = get_work_list_all()

    update_index = index - 1
    for work in works_list:
        worksheet.write(0, index, work.work_name, cell_format)
        index += 1

    works = get_work_all()

    for work in works:
        user = get_user(id_in=work.user_rel.id)
        worksheet.write(work.user_id, 0, user.user_id, cell_format)
        worksheet.write(work.user_id, 1, user.full_name, cell_format)
        worksheet.write(work.user_id, 2, user.student_number, cell_format)
        if work.score is None:
            worksheet.write(work.user_id, work.work.id + update_index, 'تصحیح نشده', cell_format)
        else:
            worksheet.write(work.user_id, work.work.id + update_index, work.score, cell_format)

    worksheet.set_column('A:W', 40)
    workbook.close()

    wb = openpyxl.load_workbook(path_xlsx)
    sheet = wb['scores']
    for i in range(20):
        for row in sheet:
            remove(sheet, row)
    wb.save(path_xlsx)
