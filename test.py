from app.physicsLab1.api import get_user
from app.physicsLab1.model.physics_user_model import  PhysicsLab1UserDB
from app.user.model.user_model import UserDB
from core.database.database import session

asd: PhysicsLab1UserDB = get_user(id_in=99981475)
print(asd.user_rel)
# session.commit()