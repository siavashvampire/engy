from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from app.physicsLab1.api import get_class, get_work_list, get_work_by_user_id, get_all_user

keyboard = [
    [
        InlineKeyboardButton("Yes", callback_data="yes"),
        InlineKeyboardButton("No", callback_data="no"),
    ]
]

ikm_yes_no = InlineKeyboardMarkup(keyboard)

keyboard = [
    [
        InlineKeyboardButton("accept", callback_data="accept"),
        InlineKeyboardButton("reject", callback_data="reject"),
    ]
]

ikm_accept_reject = InlineKeyboardMarkup(keyboard)

keyboard = [
    [
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
    ],
    [
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
        InlineKeyboardButton("6", callback_data="6"),
    ],
    [
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
    ],
    [
        InlineKeyboardButton(".", callback_data="."),
        InlineKeyboardButton("0", callback_data="0"),
        InlineKeyboardButton("Enter", callback_data="enter"),
    ],
]

ikm_full = InlineKeyboardMarkup(keyboard)


def get_ikm_physics_lab_1_class():
    physics_lab_1_classes = get_class()
    keyboard = []
    for physics_lab_1_class in physics_lab_1_classes:
        keyboard.append([InlineKeyboardButton(
            physics_lab_1_class.class_name + "\nروز " + physics_lab_1_class.class_day + " ساعت " + physics_lab_1_class.class_time,
            callback_data=physics_lab_1_class.id)])

    ikm_physics_lab_1_class = InlineKeyboardMarkup(keyboard)
    return ikm_physics_lab_1_class


def get_ikm_physics_lab_1_work_list(user_id: int):
    physics_lab_1_work_lists = get_work_list()
    physics_lab_1_work_lists_del = get_work_by_user_id(user_id)
    del_idx = []
    for idx, work in enumerate(physics_lab_1_work_lists):
        for work_del in physics_lab_1_work_lists_del:
            if work.id == work_del.work.id:
                del_idx.append(idx)

    del_idx.sort(reverse=True)
    for idx in del_idx:
        physics_lab_1_work_lists.pop(idx)

    keyboard = []
    for physics_lab_1_work_list in physics_lab_1_work_lists:
        keyboard.append(
            [InlineKeyboardButton(physics_lab_1_work_list.work_name, callback_data=physics_lab_1_work_list.id)])

    return InlineKeyboardMarkup(keyboard)


def get_ikm_physics_lab_1_user_list():
    users = get_all_user()

    keyboard = []
    for user in users:
        keyboard.append(
            [InlineKeyboardButton(user.user_rel.first_name + " " + str(user.user_rel.id), callback_data=user.user_id)])

    return InlineKeyboardMarkup(keyboard)
