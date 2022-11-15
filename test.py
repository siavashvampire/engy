# from app.physicsLab1.api import get_user
# from app.physicsLab1.model.physics_user_model import  PhysicsLab1UserDB
# from app.user.model.user_model import UserDB
# from core.database.database import session
#
# asd: PhysicsLab1UserDB = get_user(id_in=99981475)
# print(asd.user_rel)
# session.commit()
from app.physicsLab1.api import get_work_by_id
from core.style.InlineKeyboardMarkup import get_ikm_physics_lab_1_work_list
asd = get_ikm_physics_lab_1_work_list(2)
print()
# work = get_work_by_id(2)
# work.insert_data(99981475)
