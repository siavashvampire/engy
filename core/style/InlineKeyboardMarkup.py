from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from app.physicsLab1.api import get_class

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

physics_lab_1_classes = get_class()
keyboard = []
for physics_lab_1_class in physics_lab_1_classes:
    keyboard.append([InlineKeyboardButton(
        physics_lab_1_class.class_name + "\nروز " + physics_lab_1_class.class_day + " ساعت " + physics_lab_1_class.class_time,
        callback_data=physics_lab_1_class.id)])

ikm_physics_lab_1_class = InlineKeyboardMarkup(keyboard)
