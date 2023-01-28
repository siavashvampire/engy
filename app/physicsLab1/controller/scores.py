import os
from pathlib import Path

import excel2img

import xlsxwriter
from telegram import Update
from telegram.ext import CallbackContext

from app.physicsLab1.api import get_work_by_user_id, get_user

parent_path = Path(__file__).resolve().parent


def get_score(update: Update, context: CallbackContext):
    user = get_user(user=update.effective_user)
    if user.user_id == 0:
        update.message.reply_text("your are not an engy user,please start bot with command /start to join")
        return

    update.message.reply_chat_action('upload_photo')
    path = '../junk/'

    if not os.path.exists(parent_path.joinpath(path)):
        os.makedirs(parent_path.joinpath(path))
    path = parent_path.joinpath(path).resolve()
    path_xlsx = str(path.joinpath('./test.xlsx'))
    path_png = str(path.joinpath('./test.png'))

    works = get_work_by_user_id(user.user_id)
    # works = get_work_by_user_id(34)

    workbook = xlsxwriter.Workbook(path_xlsx)

    worksheet = workbook.add_worksheet('scores')
    cell_format = workbook.add_format()

    cell_format.set_align('center')
    cell_format.set_align('vcenter')

    index = 0

    worksheet.write(index, 1, 'نام آزمایش', cell_format)
    worksheet.write(index, 0, 'نمره', cell_format)
    index += 1

    for work in works:
        worksheet.write(index, 1, work.work.work_name, cell_format)
        if work.score is None:
            worksheet.write(index, 0, 'تصحیح نشده', cell_format)
        else:
            worksheet.write(index, 0, work.score, cell_format)
        index += 1

    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 40)
    workbook.close()
    excel2img.export_img(path_xlsx, path_png)

    os.remove(path_xlsx)

    update.message.reply_photo(open(path_png, 'rb'))
    os.remove(path_png)